---
attributions:
- entity:
    affiliation: null
    email: null
    name: CARI-WFP
    url: https://data.humdata.org/dataset/people-in-need-pin-del-cluster-de-seguridad-alimentaria-y-nutricion-san-sp-food-en-colombia-2022
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: SIVIGILA-INS 2020-2021
    url: https://data.humdata.org/dataset/people-in-need-pin-del-cluster-de-seguridad-alimentaria-y-nutricion-san-sp-food-en-colombia-2022
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: iMMAP Inc.
  url: https://data.humdata.org/dataset/people-in-need-pin-del-cluster-de-seguridad-alimentaria-y-nutricion-san-sp-food-en-colombia-2022
creator:
  affiliation: null
  email: null
  name: iMMAP Inc.
  url: https://data.humdata.org/dataset/people-in-need-pin-del-cluster-de-seguridad-alimentaria-y-nutricion-san-sp-food-en-colombia-2022
dataset_id: rdls_lss-col_immap_peopleneedpindelclusterde
description: "Esta base de datos contiene los c\xE1lculos de People in Need (PiN)\
  \ del Cl\xFAster de seguridad alimentaria y nutrici\xF3n (SAN-SP) (FOOD-EN) realizados\
  \ en el marco del Ciclo de Programaci\xF3n Humanitaria de Colombia para 2022.. [Source:\
  \ This metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/people-in-need-pin-del-cluster-de-seguridad-alimentaria-y-nutricion-san-sp-food-en-colombia-2022]"
details: null
exposure: []
hazard: null
license: CC0-1.0
lineage:
  description: People in Need estimates were calculated by the Food Security and Nutrition
    Cluster (SAN-SP) using CARI-WFP food insecurity classifications and SIVIGILA-INS
    malnutrition surveillance data (2020-2021) through a census-based methodology
    within Colombia's 2022 Humanitarian Programming Cycle framework.
  sources:
  - id: source_1
    license: null
    name: CARI-WFP
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: SIVIGILA-INS 2020-2021
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/people-in-need-pin-del-cluster-de-seguridad-alimentaria-y-nutricion-san-sp-food-en-colombia-2022
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People in Need due to food insecurity and malnutrition from drought-related
      agricultural failure
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
purpose: Census
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "People in Need (PiN) del Cl\xFAster de seguridad alimentaria y nutrici\xF3\
    n (SAN-SP) (FOOD-EN) - Colombia - 2022 (Nota metodol\xF3gica PiN Seguridad Alimentaria\
    \ y nutrici\xF3n - HNO 2022)"
  download_url: https://data.humdata.org/dataset/1228c7fc-2ad2-45a2-9f41-18e73f4e41fa/resource/e2df443d-502a-452d-80b8-4a3060d17027/download/nota-metodologica-pin-2022_san.pdf
  format: null
  id: resource_e2df443d
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Nota metodologica PIN 2022_SAN.pdf
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "People in Need (PiN) del Cl\xFAster de seguridad alimentaria y nutrici\xF3\
    n (SAN-SP) (FOOD-EN) - Colombia - 2022 (Base de datos de PiN en formato xlsx.)"
  download_url: https://data.humdata.org/dataset/1228c7fc-2ad2-45a2-9f41-18e73f4e41fa/resource/5db9438b-3692-4a0e-b49f-b966d96c3b41/download/pin_san_2022_hdx.xlsx
  format: null
  id: resource_5db9438b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PIN_SAN_2022_HDX.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "People in Need (PiN) del Cl\xFAster de seguridad alimentaria y nutrici\xF3\
    n (SAN-SP) (FOOD-EN) - Colombia - 2022 (Base de datos de PiN en formato csv.)"
  download_url: https://data.humdata.org/dataset/1228c7fc-2ad2-45a2-9f41-18e73f4e41fa/resource/fecfa443-1a47-4bf4-8931-8e110b2a5079/download/pin_san_2022_hdx.csv
  format: null
  id: resource_fecfa443
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PIN_SAN_2022_HDX.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "People in Need (PiN) del Cl\xFAster de seguridad alimentaria y nutrici\xF3\
    n (SAN-SP) (FOOD-EN) - Colombia - 2022 (Diccionario de Datos.)"
  download_url: https://data.humdata.org/dataset/1228c7fc-2ad2-45a2-9f41-18e73f4e41fa/resource/3023cc0a-706c-4cff-abdd-4254e5e14f8e/download/diccionario_datos_pin_food_hdx.xlsx
  format: null
  id: resource_3023cc0a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: diccionario_datos_pin_food_hdx.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-col_immap_peopleneedpindelclusterde
spatial:
  bbox: null
  centroid: null
  countries:
  - COL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: "People in Need (PiN) del Cl\xFAster de seguridad alimentaria y nutrici\xF3\
  n (SAN-SP) (FOOD-EN) - Colombia - 2022"
version: null
vulnerability: null
---
