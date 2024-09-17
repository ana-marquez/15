Copiar código
from odoo.tests.common import TransactionCase

# @tagged('-at_install', 'post_install')
class TestAnimalState(TransactionCase):
    def setUp(self, *args, **kwargs):
        super(TestAnimalState, self).setUp(*args, **kwargs)
        # Crear registros de prueba
        self.test_species = self.env["animal.species"].create({"name": "specie 1"})
        self.test_breed = self.env["animal.breed"].create(
            {"name": "breed 1", "species_id": self.test_species.id}
        )
        self.test_animal = self.env["animal"].create(
            {
                "name": "Animal 1",
                "species_id": self.test_species.id,
                "breed_id": self.test_breed.id,
            }
        )

    def test_onchange_species(self):
        """Verifica que breed_id se establece en False cuando cambia species_id."""
        self.test_animal.species_id = self.test_species.id  # Trigger onchange
        self.assertFalse(
            self.test_animal.breed_id,
            "Animal breed_id should be changed to False when species_id is updated",
        )

    def test_onchange_breed(self):
        """Verifica que color_id se establece en False cuando cambia breed_id."""
        self.test_animal.breed_id = self.test_breed.id  # Trigger onchange
        self.assertFalse(
            self.test_animal.color_id,
            "Animal color_id should be changed to False when breed_id is updated",
        )