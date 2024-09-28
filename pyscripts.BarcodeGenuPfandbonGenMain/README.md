# pyscripts.BarcodeGenuPfandbonGenMain

   ## Overview
   This module generates a Pfandbon (deposit receipt) with specific formatting and details.

   ## Installation
   ```sh
   pip install pyscripts.BarcodeGenuPfandbonGenMain ## Usage from pyscripts.BarcodeGenuPfandbonGenMain import PfandbonGenerator

   items = [{'count': 100, 'type': 'Einweg', 'unit_price': 0.25, 'total_price': 25.00}]
   generator = PfandbonGenerator(store_code='1234567', street='Musterstraße', house_number='1', postal_code='12345', city='Musterstadt', items=items, total_sum=25.00, pfandbon_number=random.randint(1000000, 9999999))
   generator.generate()
