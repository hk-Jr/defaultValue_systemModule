import sys
if len(sys.argv)==3:
  script_name=sys.argv[0]
  name=sys.argv[1]
  rollNo=sys.argv[2]
  print(f"\n\nUser details provided!!!")

else:
  script_name=sys.argv[0]
  name="king"
  rollNo=157
  print("no input given - Using default Value.")

print(f"Script name:{script_name}\nName:{name}\nRoll No:{rollNo}.")
