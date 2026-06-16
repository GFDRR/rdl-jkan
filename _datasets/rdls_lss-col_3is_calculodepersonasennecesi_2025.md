---
attributions:
- entity:
    affiliation: null
    email: null
    name: "Cl\xFAster de Agua, Saneamiento e Higiene (WASH)"
    url: https://data.humdata.org/dataset/calculo-de-personas-en-necesidad-pin-del-cluster-de-agua-saneamiento-e-higiene-wash-2026-colombia
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: "DANE (Departamento Administrativo Nacional de Estad\xEDstica)"
    url: https://data.humdata.org/dataset/calculo-de-personas-en-necesidad-pin-del-cluster-de-agua-saneamiento-e-higiene-wash-2026-colombia
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: "UNGRD (Unidad Nacional de Gesti\xF3n del Riesgo de Desastres)"
    url: https://data.humdata.org/dataset/calculo-de-personas-en-necesidad-pin-del-cluster-de-agua-saneamiento-e-higiene-wash-2026-colombia
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: MONITOR
    url: https://data.humdata.org/dataset/calculo-de-personas-en-necesidad-pin-del-cluster-de-agua-saneamiento-e-higiene-wash-2026-colombia
  id: attribution_4
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: SIVIGILA
    url: https://data.humdata.org/dataset/calculo-de-personas-en-necesidad-pin-del-cluster-de-agua-saneamiento-e-higiene-wash-2026-colombia
  id: attribution_5
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: DNP/UNGRD
    url: https://data.humdata.org/dataset/calculo-de-personas-en-necesidad-pin-del-cluster-de-agua-saneamiento-e-higiene-wash-2026-colombia
  id: attribution_6
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: 3iS
  url: https://data.humdata.org/dataset/calculo-de-personas-en-necesidad-pin-del-cluster-de-agua-saneamiento-e-higiene-wash-2026-colombia
creator:
  affiliation: null
  email: null
  name: 3iS
  url: https://data.humdata.org/dataset/calculo-de-personas-en-necesidad-pin-del-cluster-de-agua-saneamiento-e-higiene-wash-2026-colombia
dataset_id: rdls_lss-col_3is_calculodepersonasennecesi_2025
description: "Esta base contiene el resultado final del c\xE1lculo las Personas en\
  \ Necesidad (PiN), las severidades y las desagregaciones poblacionales para el Cl\xFA\
  ster de Agua, Saneamiento e Higiene (WASH) en Colombia, 2026.. [Source: This metadata\
  \ record was automatically extracted from the Humanitarian Data Exchange (HDX);\
  \ Original dataset: https://data.humdata.org/dataset/calculo-de-personas-en-necesidad-pin-del-cluster-de-agua-saneamiento-e-higiene-wash-2026-colombia]"
details: null
exposure: []
hazard: null
license: CC0-1.0
lineage:
  description: The dataset integrates population baseline data from DANE with multi-sectoral
    WASH indicators (water access, sanitation, waste collection), health surveillance
    data (SIVIGILA disease rates, malnutrition), and disaster exposure records (UNGRD
    2024-2025, MONITOR) at municipal level. Severity scores are calculated for each
    indicator, weighted and adjusted using institutional capacity indices (DNP/UNGRD)
    and water quality indices (IRCA), then aggregated with expert judgment to produce
    final severity classifications and People in Need estimates for 2026.
  sources:
  - id: source_1
    license: null
    name: "Cl\xFAster de Agua, Saneamiento e Higiene (WASH)"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: "DANE (Departamento Administrativo Nacional de Estad\xEDstica)"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: "UNGRD (Unidad Nacional de Gesti\xF3n del Riesgo de Desastres)"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_4
    license: null
    name: MONITOR
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_5
    license: null
    name: SIVIGILA
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_6
    license: null
    name: DNP/UNGRD
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/calculo-de-personas-en-necesidad-pin-del-cluster-de-agua-saneamiento-e-higiene-wash-2026-colombia
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People in Need (PiN) due to inadequate water, sanitation and hygiene
      access in Colombia 2026
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://reliefweb.int/report/colombia/nota-metodologica-calculo-de-personas-en-necesidad-pin-del-cluster-de-agua-saneamiento-e-higiene-wash-2026-colombia
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Esta base contiene el resultado final del c\xE1lculo las Personas\
    \ en Necesidad (PiN), las severidades y las desagregaciones poblacionales para\
    \ el Cl\xFAster de Agua, Saneamiento e Higiene (WASH) en Colombia, 2026. Para\
    \ m\xE1s informaci\xF3n, por favor consulte la nota metodol\xF3gica."
  download_url: https://data.humdata.org/dataset/3c140b0b-37ce-4bba-9bdf-fc4a2f3dd486/resource/1e111e55-2418-4640-89fe-8c53b3532a98/download/desagregacion-pin-wash-colombia-2026.xlsx
  format: null
  id: resource_1e111e55
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "Desagregacio\u0301n PiN WASH - Colombia 2026.xlsx"
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-col_3is_calculodepersonasennecesi_2025
spatial:
  bbox: null
  centroid: null
  countries:
  - COL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-12-31'
  start: '2025-06-01'
temporal_resolution: null
title: "Colombia: C\xE1lculo de Personas en Necesidad (PiN) del Cl\xFAster de Agua,\
  \ Saneamiento e Higiene (WASH)"
version: null
vulnerability: null
---
