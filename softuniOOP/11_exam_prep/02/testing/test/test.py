from unittest import TestCase, main

from project.gallery import Gallery


class TestGallery(TestCase):
    def setUp(self):
        self.test_gallery = Gallery("Hm", "Pogapolis", 10.5)
        self.test_gallery.exhibitions = {"ok": 2000, "k": 1000}

    def test_init(self):
        self.assertEqual("Hm", self.test_gallery.gallery_name)
        self.assertEqual("Pogapolis", self.test_gallery.city)
        self.assertEqual(10.5, self.test_gallery.area_sq_m)
        self.assertTrue(self.test_gallery.open_to_public)
        self.assertEqual({"ok": 2000, "k": 1000}, self.test_gallery.exhibitions)

    def test_init_creating_object_with_false(self):
        gallery = Gallery("a", "b", 1.4, False)
        self.assertEqual("a", gallery.gallery_name)
        self.assertEqual("b", gallery.city)
        self.assertEqual(1.4, gallery.area_sq_m)
        self.assertFalse(gallery.open_to_public)
        self.assertEqual({}, gallery.exhibitions)

    def test_gallery_name_setter_errors(self):
        with self.assertRaises(ValueError) as ve:
            self.test_gallery.gallery_name = "h!m"
        self.assertEqual("Gallery name can contain letters and digits only!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.test_gallery.gallery_name = "    "
        self.assertEqual("Gallery name can contain letters and digits only!", str(ve.exception))

    def test_city_setter_errors(self):
        with self.assertRaises(ValueError) as ve:
            self.test_gallery.city = ""
        self.assertEqual("City name must start with a letter!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.test_gallery.city = "5lmao"
        self.assertEqual("City name must start with a letter!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.test_gallery.city = "?lol"
        self.assertEqual("City name must start with a letter!", str(ve.exception))

    def test_area_sq_m_setter_errors(self):
        with self.assertRaises(ValueError) as ve:
            self.test_gallery.area_sq_m = 0
        self.assertEqual("Gallery area must be a positive number!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.test_gallery.area_sq_m = -1
        self.assertEqual("Gallery area must be a positive number!", str(ve.exception))

    def test_add_exhibition_existing(self):
        result = self.test_gallery.add_exhibition("ok", 1000)
        self.assertEqual('Exhibition "ok" already exists.', result)

    def test_add_exhibition_valid(self):
        result = self.test_gallery.add_exhibition("lol", 2000)
        self.assertEqual('Exhibition "lol" added for the year 2000.', result)
        self.assertEqual({"ok": 2000, "k": 1000, "lol": 2000}, self.test_gallery.exhibitions)

    def test_remove_exhibition_non_existing(self):
        result = self.test_gallery.remove_exhibition("a")
        self.assertEqual('Exhibition "a" not found.', result)

    def test_remove_exhibition_valid(self):
        result = self.test_gallery.remove_exhibition("ok")
        self.assertEqual('Exhibition "ok" removed.', result)
        self.assertEqual({"k": 1000}, self.test_gallery.exhibitions)

    def test_list_exhibition_open_gallery(self):
        result = self.test_gallery.list_exhibitions()
        self.assertEqual("ok: 2000\nk: 1000", result)

    def test_list_exhibition_closed_gallery(self):
        self.test_gallery.open_to_public = False
        self.assertFalse(self.test_gallery.open_to_public)
        result = self.test_gallery.list_exhibitions()
        self.assertEqual('Gallery Hm is currently closed for public! Check for updates later on.', result)


if __name__ == "__main__":
    main()
