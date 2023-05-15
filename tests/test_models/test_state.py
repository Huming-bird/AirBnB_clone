#!/usr/bin/python3
"""Defines unittests for models/state.py.

Unittest classes:
    TestState_instantiation
    TestState_save
    TestState_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State


class TestState_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the State class."""

    def test_no_args_instantiates(self):
        """test instanciation with no args"""
        self.assertEqual(State, type(State()))

    def test_new_instance_stored_in_objects(self):
        """Test id an instance is corretly store"""
        self.assertIn(State(), models.storage.all().values())

    def test_id_is_public_str(self):
        """test type of an attribute"""
        self.assertEqual(str, type(State().id))

    def test_created_at_is_public_datetime(self):
        """test type of an attribute"""
        self.assertEqual(datetime, type(State().created_at))

    def test_updated_at_is_public_datetime(self):
        """test type of an attribute"""
        self.assertEqual(datetime, type(State().updated_at))

    def test_name_is_public_class_attribute(self):
        """test if an attribute is public"""
        cy = State()
        self.assertEqual(str, type(State.name))
        self.assertIn("name", dir(cy))
        self.assertNotIn("name", cy.__dict__)

    def test_two_states_unique_ids(self):
        """Test if two states have differents id"""
        cy1 = State()
        cy2 = State()
        self.assertNotEqual(cy1.id, cy2.id)

    def test_two_states_different_created_at(self):
        """test if two states have different creation date"""
        cy1 = State()
        sleep(0.05)
        cy2 = State()
        self.assertLess(cy1.created_at, cy2.created_at)

    def test_two_states_different_updated_at(self):
        """Test if two states have differents update date"""
        cy1 = State()
        sleep(0.05)
        cy2 = State()
        self.assertLess(cy1.updated_at, cy2.updated_at)

    def test_str_representation(self):
        """test the string representation of a state"""
        dt = datetime.today()
        dt_repr = repr(dt)
        cy = State()
        cy.id = "123456"
        cy.created_at = cy.updated_at = dt
        cystr = cy.__str__()
        self.assertIn("[State] (123456)", cystr)
        self.assertIn("'id': '123456'", cystr)
        self.assertIn("'created_at': " + dt_repr, cystr)
        self.assertIn("'updated_at': " + dt_repr, cystr)

    def test_args_unused(self):
        """Test argumenst that are not used"""
        cy = State(None)
        self.assertNotIn(None, cy.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """Test instanciation with kwargs"""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        cy = State(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(cy.id, "345")
        self.assertEqual(cy.created_at, dt)
        self.assertEqual(cy.updated_at, dt)


class TestState_save(unittest.TestCase):
    """Unittests for testing save method of the State class."""

    @classmethod
    def setUp(self):
        """create an example of file"""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        """delete json file"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        """test id a instance is save once"""
        cy = State()
        sleep(0.05)
        first_updated_at = cy.updated_at
        cy.save()
        self.assertLess(first_updated_at, cy.updated_at)

    def test_two_saves(self):
        """test if an instance is save second time"""
        cy = State()
        sleep(0.05)
        first_updated_at = cy.updated_at
        cy.save()
        second_updated_at = cy.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        cy.save()
        self.assertLess(second_updated_at, cy.updated_at)

    def test_save_with_arg(self):
        """test the save method with arg"""
        cy = State()
        with self.assertRaises(TypeError):
            cy.save(None)

    def test_save_updates_file(self):
        """test update of json file when saving an instance"""
        cy = State()
        cy.save()
        cyid = "State." + cy.id
        with open("file.json", "r") as f:
            self.assertIn(cyid, f.read())


class TestState_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the State class."""

    def test_to_dict_type(self):
        """test structure of dictionnary"""
        self.assertTrue(dict, type(State().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        """Test if keys in dict are corrects"""
        cy = State()
        self.assertIn("id", cy.to_dict())
        self.assertIn("created_at", cy.to_dict())
        self.assertIn("updated_at", cy.to_dict())
        self.assertIn("__class__", cy.to_dict())

    def test_to_dict_contains_added_attributes(self):
        """test added attributes in dit"""
        cy = State()
        cy.middle_name = "Holberton"
        cy.my_number = 98
        self.assertEqual("Holberton", cy.middle_name)
        self.assertIn("my_number", cy.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        """test type of date in dictionnary"""
        cy = State()
        cy_dict = cy.to_dict()
        self.assertEqual(str, type(cy_dict["id"]))
        self.assertEqual(str, type(cy_dict["created_at"]))
        self.assertEqual(str, type(cy_dict["updated_at"]))

    def test_to_dict_output(self):
        """test the uotput of dictionnray"""
        dt = datetime.today()
        cy = State()
        cy.id = "123456"
        cy.created_at = cy.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'State',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(cy.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        """test contrast between dict() and __dit__"""
        cy = State()
        self.assertNotEqual(cy.to_dict(), cy.__dict__)

    def test_to_dict_with_arg(self):
        """Test dictionnary with args"""
        cy = State()
        with self.assertRaises(TypeError):
            cy.to_dict(None)


if __name__ == "__main__":
    unittest.main()
