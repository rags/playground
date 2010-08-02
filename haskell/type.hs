type CardHolder = String
type CardNumber = String
type CustInfo = (String,String)

data BillInfo = CreditCard CardHolder CardNumber | Cash CustInfo deriving (Show)