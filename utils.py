# utils.py

# Lists
# Required for SDS and Chemical name
hazards_fields = [
    "chemical_name",
    "sds_reference"
]

waste_disposal_measures_fields = [
    "chemical_name"
]
spill_management_fields = [
    "chemical_name"
]

fire_procedures_fields = [
    "chemical_name"
]
first_aid_procedures_fields = [
    "chemical_name"
]

storage_fields = [
    "chemical_name"
]

lista_tablas = [
    "Hazards",
    "Waste disposal measures, disposal waste",
    "Spill management, spills, information_and_details_about_Spill_management",
    "Fire procedures, Fire Fighting Measures, information_and_details_about_Fire_procedures",
    "First aid procedures, First Aid Measures",
    "Storage, Safe Storage"
    ]

# Required for Control Measures
hazards_fields = [
    "explosive",
    "flammable",
    "oxidising",
    "gas_under_pressure",
    "acute_toxicity",
    "corrosive",
    "health_hazard",
    "serious_health_hazard",
    "hazardous_to_the_environment"
]
hazards_protection_measures_fields = [
    "wear_full_face_visor",
    "box_goggles_must_be_worn",
    "protective_gloves_must_be_worn",
    "laboratory_coats_must_be_worn",
    "use_local_exhaust_ventillation",
    "no_open_flames",
    "other_control_measures"
]
# Patterns by PPE field (for cleaning and exclusion)
_FIELD_PATTERNS = {
    "wear_full_face_visor": [r"\bface\s*shield\b", r"\bfull\s*face\s*visor\b"],
    "box_goggles_must_be_worn": [r"\bgoggles\b", r"\bsafety\s*glasses\b", r"\beye\s*protection\b"],
    "protective_gloves_must_be_worn": [r"\bprotective\s*gloves\b", r"\bhand\s*protection\b", r"\bgloves\b", r"\bnitrile\b", r"\bbutyl\b"],
    "laboratory_coats_must_be_worn": [r"\blab\s*coat\b", r"\bprotective\s*clothing\b", r"\bbody\s*protection\b"],
    "use_local_exhaust_ventillation": [r"\blocal\s*exhaust\s*ventilation\b", r"\bLEV\b", r"\bfume\s*hood\b"],
    "no_open_flames": [r"\bno\s*open\s*flames\b", r"\bignition\s*sources\b", r"\bkeep\s*away\s*from\s*ignition\b", r"\bnon\-?sparking\s*tools?\b"],
}

PPE_FIELDS = [
    "wear_full_face_visor",
    "box_goggles_must_be_worn",
    "protective_gloves_must_be_worn",
    "laboratory_coats_must_be_worn",
    "use_local_exhaust_ventilation",
    "no_open_flames",
]

# Required for Hazards
hazards_fields_statements = [
    "explosive",
    "flammable",
    "oxidising",
    "gas_under_pressure",
    "acute_toxicity",
    "corrosive",
    "health_hazard",
    "serious_health_hazard",
    "hazardous_to_the_environment"
]

# Required for Storage
# STORAGE Fields
STORAGE_FIELDS = [
    "flammables_cupboard",
    "corrosives_cupboard",
    "poisons_cupboard",
    "ventilated_storage",
    "gas_cylinder",
    "cold_storage",
    "dessicated_storage",
]

# Patterns by field (to search for evidence in the base text)
_STORAGE_PATTERNS = {
    "flammables_cupboard": [
        r"\bflammable(s)?\b", r"\bflammables\s*cupboard\b",
        r"\bstore in flammables?( cabinet| cupboard)?\b",
        r"\bkeep away from (heat|open flames|ignition sources)\b",
    ],
    "corrosives_cupboard": [
        r"\bcorrosive(s)?\b", r"\bcorrosives?\s*(cupboard|cabinet)\b",
        r"\bstore in (a )?corrosives? (cabinet|cupboard)\b",
        r"\bacids?\b", r"\bbases?\b",
    ],
    "poisons_cupboard": [
        r"\bpoison(s|ous)?\b", r"\btox(ic|icity)\b",
        r"\bpoisons?\s*(cupboard|cabinet)\b",
        r"\bstore in locked (cabinet|cupboard)\b",
    ],
    "ventilated_storage": [
        r"\bventilated storage\b", r"\bventilated area\b",
        r"\bstore in a well-ventilated place\b", r"\bKEEP CONTAINER TIGHTLY CLOSED IN A WELL-VENTILATED PLACE\b",
        r"\blocal exhaust\b", r"\bfume hood\b",
    ],
    "gas_cylinder": [
        r"\bgas cylinder(s)?\b", r"\bcompressed gas(es)?\b", r"\bpressurized\b",
        r"\bsecure cylinder(s)?\b", r"\bupright\b", r"\bcap(s)? in place\b",
    ],
    "cold_storage": [
        r"\bcold storage\b", r"\brefrigerate(d)?\b", r"\bstore (at|below) \d+ ?°?C\b",
        r"\btemperature control\b",
    ],
    "dessicated_storage": [
        r"\bdessicat(ed|ion)?\b", r"\bdesiccator\b", r"\bdry storage\b",
        r"\bkeep dry\b", r"\bprotect from moisture\b", r"\bmoisture sensitive\b",
    ],
}

# Required for Hazards Text
hazards_fields_dtr = [
    "physical_form_and_quantity",
    "potential_routes_of_exposure",
    "workplace_exposure_limits",
    "arising_harm"
]

waste_disposal_measures_fields_dtr = [
    "handling_of_the_product_if_it_becomes_waste"
]

spill_management_fields_dtr = [
    "details"
]

fire_procedures_fields_dtr = [
    "details"
]

first_aid_procedures_fields_dtr = [
    "eyes",
    "skin",
    "if_ingested",
    "if_inhaled"
]

storage_fields_dtr = [
    "hazard_label_and_store_safely_on_shelf",
    "special_storage_describe"
]

dtr_tables = [
    "Hazards",
    "Waste disposal measures, disposal waste",
    "Spill management, spills, information_and_details_about_Spill_management",
    "Fire procedures, Fire Fighting Measures, information_and_details_about_Fire_procedures",
    "First aid procedures, First Aid Measures",
    "Storage, Safe Storage"
]