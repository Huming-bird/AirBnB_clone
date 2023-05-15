#!/usr/bin/python3

import unittest
import sys
import io
from contextlib import contextmanager
from unittest.mock import patch
from io import StringIO
from models import *
from datetime import datetime
from console import HBNBCommand
from models.base_model import BaseModel


class Test_Console(unittest.TestCase):
    """
    Test the console
    """

    def setUp(self):
        self.cli = HBNBCommand()

        test_args = {'updated_at': datetime(2017, 2, 11, 23, 48, 34, 339879),
                     'id': 'd3da85f2-499c-43cb-b33d-3d7935bc808c',
                     'created_at': datetime(2017, 2, 11, 23, 48, 34, 339743),
                     'name': 'Ace'}
        self.model = BaseModel(test_args)
        self.model.save()

    def tearDown(self):
        with patch('sys.stdout', new=StringIO()) as f:
            com = "destroy BaseModel d3da85f2-499c-43cb-b33d-3d7935bc808c"
            self.cli.onecmd(com)

    def test_show_error_no_args(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("show ''")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_show_error_missing_arg(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("show BaseModel")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_show_error_invalid_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("show Human 1234-5678-9101")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create BaseModel")
            output = f.getvalue()

        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("show BaseModel {}".format(output))
        self.assertFalse(output in f.getvalue())

    def test_destroy_correct(self):
        test_args = {'updated_at': datetime(2017, 2, 12, 00, 31, 53, 331997),
                     'id': 'f519fb40-1f5c-458b-945c-2ee8eaaf4900',
                     'created_at': datetime(2017, 2, 12, 00, 31, 53, 331900)}
        testmodel = BaseModel(test_args)
        testmodel.save()
        with patch('sys.stdout', new=StringIO()) as f:
            com = "destroy BaseModel f519fb40-1f5c-458b-945c-2ee8eaaf4900"
            self.cli.onecmd(com)

        with patch('sys.stdout', new=StringIO()) as f:
            com = "show BaseModel f519fb40-1f5c-458b-945c-2ee8eaaf4900"
            self.cli.onecmd(com)
            self.assertEqual(f.getvalue(), "** no instance found **\n")

    def test_destroy_error_missing_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("destroy BaseModel")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_destroy_error_invalid_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            com = "destroy Human d3da85f2-499c-43cb-b33d-3d7935bc808c"
            self.cli.onecmd(com)
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_destroy_error_invalid_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            com = "destroy BaseModel f519fb40-1f5c-458b-945c-2ee8eaaf4900"
            self.cli.onecmd(com)
            self.assertEqual(f.getvalue(), "** no instance found **\n")

    def test_all_correct(self):
        test_args = {'updated_at': datetime(2017, 2, 12, 00, 31, 53, 331997),
                     'id': 'f519fb40-1f5c-458b-945c-2ee8eaaf4900',
                     'created_at': datetime(2017, 2, 12, 00, 31, 53, 331900)}
        testmodel = BaseModel(test_args)
        testmodel.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("all")
            self.assertFalse("123-456-abc" in f.getvalue())

    def test_all_error_invalid_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("all Human")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            com = "show BaseModel d3da85f2-499c-43cb-b33d-3d7935bc808c"
            self.cli.onecmd(com)
            self.assertFalse("Ace" in f.getvalue())

    def test_update_error_invalid_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("update BaseModel 123-456-abcic name Cat")
            self.assertEqual(f.getvalue(), "** no instance found **\n")

    def test_update_error_invalid_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            com = "update Human d3da85f2-499c-43cb-b33d-3d7935bc808c name Cat"
            self.cli.onecmd(com)
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_update_error_missing_value(self):
        with patch('sys.stdout', new=StringIO()) as f:
            com = "update BaseModel d3da85f2-499c-43cb-b33d-3d7935bc808c name"
            self.cli.onecmd(com)
            self.assertEqual(f.getvalue(), "** value missing **\n")


if __name__ == "__main__":
    unittest.main()
