import unittest
from app.Unifier import Unifier



class TestScraper(unittest.TestCase):
    def test_private_seller(self):
        cut = Unifier()
        exp = "Private"
        act = cut.unify("PrivateSeller")

        self.assertEqual(exp, act)
    
    def test_oruvate(self):
        cut = Unifier()
        exp = "Private"
        act = cut.unify("Private")

        self.assertEqual(exp, act)

    def test_format_phone_number(self):
        # 015759546159 -> +49015759546159
        phone = ['015759546159']
        cut = Unifier()
        
        act = cut.unify_phone_number(phone)
        exp = ['+49015759546159']
        
        self.assertEqual(act, exp)

    def test_format_phone_number_with_empty_string(self):
        phone = [ '' ]
        cut = Unifier()
        
        act = cut.unify_phone_number(phone)
        exp = []
        
        self.assertEqual(act, exp)

    def test_format_phone_number_with_none(self):
        phone = [ None ]
        cut = Unifier()
        
        act = cut.unify_phone_number(phone)
        exp = []
        
        self.assertEqual(act, exp)
            

    def test_format_duplica_phone_number(self):
        cut = Unifier()

        phones = ['015759546159', '015759546159']       
        act = cut.unify_phone_number(phones)
        exp = ['+49015759546159']
        
        self.assertEqual(act, exp)




        phones = [
            "+49 01729368662",
            "+49 021032530455",
            "+4901729368662"
            ]
        
        act = cut.unify_phone_number(phones)
        exp = ['+4901729368662', '+49021032530455']

        self.assertEqual(exp, act)

        phones = ["+492811479209604"]
        act = cut.unify_phone_number(phones)
        exp = ['+4902811479209604']

        self.assertEqual(exp, act)

    def test_format_phone_number_non_german(self):
        cut = Unifier()
        
        phones = [ "+370 686 54664" ]
        act = cut.unify_phone_number(phones)
        exp = [ "+37068654664" ]
        
        self.assertEqual(act, exp)

    def test_poland_phone_number(self):
        cut = Unifier()
        
        phones = [ "+40752410405" ]
        act = cut.unify_phone_number(phones)
        exp = [ "+40752410405" ]
        
        self.assertEqual(act, exp)

    def test_unify_fuel_type(self):
        cut = Unifier()

        body_type = "MPV / minivan"
        exp = 'Van Kleinbus'
        act = cut.unify_body_type(body_type)

        self.assertEqual(exp, act)

    def test_unify_technical_data(self):
        cut = Unifier()

        technical_data = [
            {
                'tag': 'field_body_type_id', 
                'label': 'Body type',
                'value': 'Saloon / sedan'
            }
        ]

        exp = [
            {
                'tag': 'bodyType', 
                'label': 'Fahrzeugtyp',
                'value': 'Limousine'
            }
        ]

        act = cut.unify_technical_data(technical_data)

        self.assertEqual(exp, act)