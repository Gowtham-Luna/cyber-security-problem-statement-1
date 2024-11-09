#!/usr/bin/python3

import sys
import random

from .utils import err_exit

# Module for colors
try:
    from rich import print
except:
    err_exit("Error: >rich< module not found.")

# Colors
re = "[bold red]"
cy = "[bold cyan]"
wh = "[white]"
gr = "[bold green]"
ma = "[bold magenta]"
ye = "[bold yellow]"
bl = "[bold blue]"

banner2=f"""
 '##::::'##::::::::::'########::'##::::::::'#######:::'######::'##:::'##:
 ##:::: ##:::::::::: ##.... ##: ##:::::::'##.... ##:'##... ##: ##::'##::
 ##:::: ##:::::::::: ##:::: ##: ##::::::: ##:::: ##: ##:::..:: ##:'##:::
 ##:::: ##:'#######: ########:: ##::::::: ##:::: ##: ##::::::: #####::::
. ##:: ##::........: ##.... ##: ##::::::: ##:::: ##: ##::::::: ##. ##:::
:. ## ##:::::::::::: ##:::: ##: ##::::::: ##:::: ##: ##::: ##: ##:. ##::
::. ###::::::::::::: ########:: ########:. #######::. ######:: ##::. ##:
:::...::::::::::::::........:::........:::.......::::......:::..::::..::
                                                                        
                              |             |
  {wh}malware analysis tool.{ye}| {wh}by BLACK INTRUDERS {ye}| {wh}Version: {gr}
  {ye}---------------------------------|             |{wh}\n
"""
banner1=f"""
        {ma}:ooooo/        /ooooo:
           +MMd^^^^^^^^hMMo			 KISHAN : GOWTHAM : SURYA : NISHAN
        oNNNMMMNNNNNNNNMMMNNNs
     /oodMMdooyMMMMMMMMyoodMMdoo/      {wh}+-----------------------------------------+
   {ma}..dMMMMMy. :MMMMMMMM/  sMMMMMm..    {wh}|              {gr}v-block                 {wh}|
  {ma}dmmMMMMMMNmmNMMMMMMMMNmmNMMMMMMmmm   {wh}|                                         |
  {ma}NMMyoodMMMMMMMMMMMMMMMMMMMMdoosMMM   {wh}|    {gr}	malware analysis tool.    {wh}|
  {ma}NMM-  sMMMNNNNNNNNNNNNNNNMMy  .MMM   {wh}|                                         |
  {ma}NMM-  sMMyvvvvvvvvvvvvvvsMMy  .MMM   {wh}|             {gr}Version{wh}: {ye}1.8.4              {wh}|
  {ma}ooo.  :ooooooo+    +ooooooo/   ooo   {wh}+-----------------|||||||-----------------+
           {ma}/MMMMN    mMMMM+                              {wh}|||||||
                                                         |||||||\n
"""
banner3=f"""
                   {wh}<------------------------------------------>
                   <  This tool is very dangerous. Be careful >
           {gr}__      {wh}<   while using it!!                       >
         {gr}_|  |_    {wh}<------------------------------------------>
       {gr}_|      |_   {wh}/
      {gr}|  _    _  | {wh}/
      {gr}| |_|  |_| |
   _  |  _    _  |  _
  |_|_|_| |__| |_|_|_|
    |_|_        _|_|   {wh}<- LUNA : NISHAN : KISHAN : SURYA
      {gr}|_|      |_|{wh} \n
"""
banner4=f"""
\n{ye}+ ------------------------------ +
I                                I
I      {wh}*********************     {ye}I
I      {wh}*  {re}MALWARE ALERT!!  {wh}*     {ye}I
I      {wh}*********************     {ye}I
I                                I
+ --------------I I------------- +
                I I                 {gr}___V-BLOCK___
                {ye}I I
             ____V_____              {ma}Version: {re}1.8.4{wh}\n\n
"""
banner5=f"""
                        {re}* -------------------------------- *
           {gr}__           {re}| {gr}Name: {wh}Mr. KISHAN                  {re}|
         {gr}_|  |_         {re}| {gr}Type: {wh}Trojan.Dropper             {re}|
       {gr}_|      |_       {re}| {gr}Status: {wh}V-BLOCKEd!!            {re}|
      {gr}|          |      {re}| {gr}Description: {wh}He said dont use    {re}|
      {gr}|  {re}X    X  {gr}|      {re}| {wh}this tool. Now he is dead.       {re}|
   {gr}_  |  _    _  |  _   {re}* -------------------------------- *
  {gr}|_|_|_| |__| |_|_|_|
    |_|_        _|_|		KISHAN : GOWTHAM : SURYA : NISHAN
      |_|      |_|{wh} \n
"""
banner6=f"""
\n{cy}LUNA SAYS:\n
         {gr}-o          o-
          +hydNNNNdyh+          {wh}<--------------------------->
        {gr}+mMMMMMMMMMMMMm+        {wh}<  Do not click every link. >
       {gr}dMM{wh}m:{gr}NMMMMMMN{wh}:m{gr}MMb       {wh}<      Please listen me!!   >
      {gr}hMMMMMMMMMMMMMMMMMMh      {wh}<--------------------------->
  {gr}..  yyyyyyyyyyyyyyyyyyyy  ..    {wh}/
{gr}.mMMm MMMMMMMMMMMMMMMMMMMM mMMm. {wh}/
{gr}:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
-MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM-
 +yy+ MMMMMMMMMMMMMMMMMMMM +yy+  {wh}<- SURYA : NISHAN : KISHAN : GOWTHAM
      {gr}mMMMMMMMMMMMMMMMMMMm
       /++MMMMh++hMMMM++/
          MMMMo  oMMMM
          MMMMo  oMMMM
          oNMm-  -mMNs{wh} \n
"""
banner7=f"""
\n  .-------------------------------------.
  | [____{re}DOWNLOADING FREE RTX 4090{wh}____] |
  |  _________________________________  |
  | |{gr}:::::::::::::::::{wh}60%{gr}|{wh}            | |
  |  \"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"  |
  |_____________________________________|\n
"""
banner8=f"""
{gr}                            .oodMMMM
                   .oodMMMMMMMMMMMMM
{re}       ..oodMMM{gr}  MMMMMMMMMMMMMMMMMMM
{re} oodMMMMMMMMMMM{gr}  MMMMMMMMMMMMMMMMMMM
{re} MMMMMMMMMMMMMM{gr}  MMMMMMMMMMMMMMMMMMM
{re} MMMMMMMMMMMMMM{gr}  MMMMMMMMMMMMMMMMMMM        {wh}One day Windows will be {gr}MALWAREPROOF{wh}...
{re} MMMMMMMMMMMMMM{gr}  MMMMMMMMMMMMMMMMMMM
{re} MMMMMMMMMMMMMM{gr}  MMMMMMMMMMMMMMMMMMM
{re} MMMMMMMMMMMMMM{gr}  MMMMMMMMMMMMMMMMMMM                      {wh}Just kidding...
					    
{cy} MMMMMMMMMMMMMM{ye}  MMMMMMMMMMMMMMMMMMM
{cy} MMMMMMMMMMMMMM{ye}  MMMMMMMMMMMMMMMMMMM
{cy} MMMMMMMMMMMMMM{ye}  MMMMMMMMMMMMMMMMMMM		  KISHAN : GOWTHAM : SURYA : NISHAN
{cy} MMMMMMMMMMMMMM{ye}  MMMMMMMMMMMMMMMMMMM
{cy} MMMMMMMMMMMMMM{ye}  MMMMMMMMMMMMMMMMMMM
{cy} `^^^^^^MMMMMMM{ye}  MMMMMMMMMMMMMMMMMMM
{cy}       ````^^^^{ye}  ^^MMMMMMMMMMMMMMMMM
                      ````^^^^^^MMMM{wh}
"""
banner9=f"""
       {re}_______________
      |{cy}@@@@{re}|     |{cy}####{re}|
      |{cy}@@@@{re}|     |{cy}####{re}|
      |{cy}@@@@{re}|     |{cy}####{re}|
      \\\{cy}@@@@{re}|     |{cy}####{re}/
       \\\{cy}@@@{re}|     |{cy}###{re}/
        `{cy}@@{re}|_____|{cy}##{re}'
             {ma}(O)
        {ye}.-''''''''''-.             {gr}Congratulations!{ye}
      .'  * * * * * * `.
     :  *             * :                  {gr}You just analyzed your 10000th sample :){ye}
    : ~ Malware Hunter ~ :
    :         of         :
    :    ~ The Year ~    :             {gr}You won 100BTC!!!{ye}
     :  *             * :
      `.  * * * * * * .'	   KISHAN : GOWTHAM : SURYA : NISHAN
        `-..........-'
"""
banner10=f"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⣤⣶⣶⣿⣷⣆⠀⠀⠀⠀
⠀⠀⠀⢀⣤⣤⣶⣶⣾⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⡆⠀⠀⠀
⠀⢀⣴⣿⣿⣿⣿⣿⣿⡿⠛⠉⠉⠀⠀⠀⣿⣿⣿⣿⣷⠀⠀⠀        {ye}!!WARNING!!{wh}: Press {re}F key{wh} to respect who clicked this link:
⣠⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⢤⣶⣾⠿⢿⣿⣿⣿⣿⣇⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠈⠉⠀⠀⠀⣿⣿⣿⣿⣿⡆⠀                  -->  {gr}https://youtu.be/lhmIH3gYaHg?si=-PdL9tgZAprWfpUP{wh}
⢸⣿⣿⣿⣏⣿⣿⣿⣿⣿⣷⠀⠀⢠⣤⣶⣿⣿⣿⣿⣿⣿⣿⡀
⠀⢿⣿⣿⣿⡸⣿⣿⣿⣿⣿⣇⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣧
⠀⠸⣿⣿⣿⣷⢹⣿⣿⣿⣿⣿⣄⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿	KISHAN : GOWTHAM : SURYA : NISHAN
⠀⠀⢻⣿⣿⣿⡇⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠘⣿⣿⣿⣿⠘⠻⠿⢛⣛⣭⣽⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⢹⣿⣿⠏⠀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠋
⠀⠀⠀⠈⣿⠏⠀⣰⣿⣿⣿⣿⣿⣿⠿⠟⠛⠋⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⡿⠿⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

randomBanner = random.randint(1, 10)
if randomBanner == 1:
    print(banner1)
elif randomBanner == 2:
    print(banner2)
elif randomBanner == 3:
    print(banner3)
elif randomBanner == 4:
    print(banner4)
elif randomBanner == 5:
    print(banner5)
elif randomBanner == 6:
    print(banner6)
elif randomBanner == 7:
    print(banner7)
elif randomBanner == 8:
    print(banner8)
elif randomBanner == 9:
    print(banner9)
elif randomBanner == 10:
    print(banner10)
else:
    pass
