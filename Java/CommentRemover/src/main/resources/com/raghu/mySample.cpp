static const char kDefaultDeathTestStyle[] = "fast//not a comment"; //comment1
//comment2
static const char kDefaultDeathTestStyle1[] = "fast/*not a comment*/";
/*comment 3*/
/*static const char kDefaultDeathTestStyle[] = "fast //not a comment"; */
/*static const char kDefaultDeathTestStyle[] = "fast /*not a comment*///";   //2 adjacent comemnts
static const char kDefaultDeathTestStyle3[] = "some" +  //remove me
"Complicated /*no comemnt*/" +               /*comment*/
"mixture";                           /*bl//ah*/    /////remove me
static const char kDefaultDeathTestStyle3[] = "done";
