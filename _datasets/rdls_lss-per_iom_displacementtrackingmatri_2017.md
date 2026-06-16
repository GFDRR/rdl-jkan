---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/peru-dtmr3
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/peru-dtmr3
dataset_id: rdls_lss-per_iom_displacementtrackingmatri_2017
description: "Displacement Tracking Matrix (DTM) R3 in Peru is a representative study\
  \ of the displaced population in the shelters of the districts of Catacaos and Cura\
  \ Mori in Piura, Peru. La Matriz de Monitoreo de Desplazamiento (DTM) R3 en Per\xFA\
  \ es un estudio representativo de la poblaci\xF3n desplazada en los albergues de\
  \ los distritos de Catacaos y Cura Mori en Piura, Per\xFA.. [Source: This metadata\
  \ record was automatically extracted from the Humanitarian Data Exchange (HDX);\
  \ Original dataset: https://data.humdata.org/dataset/peru-dtmr3]"
details: "In the DTM3 Peru Survey file, you may see some questions that are not included\
  \ in the database. This information is protected and excluded from the database\
  \ in terms of protecting the privacy of our informants.If you still need this information\
  \ please contact the OIM offices in Lima, Peru (IOMPeru@iom.int) _______________________________________________________________\
  \ En el archivo DTM3 Peru Survey, usted encontrar\xE1 algunas preguntas que no est\xE1\
  n incluidas en la base de datos. Esta informaci\xF3n est\xE1 protegida y excluida\
  \ de la base de datos por pol\xEDticas protecci\xF3n de la privacidad de nuestros\
  \ informantes. Si usted necesita esa informaci\xF3n es necesario que se contacte\
  \ con OIM Per\xFA (IOMPeru@iom.int)"
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: "The DTM R3 dataset is a representative sample survey of displaced\
    \ populations in shelters across two districts in Piura, Peru, conducted by IOM\
    \ to document displacement impacts from El Ni\xF1o-related flooding events. Survey\
    \ data was collected and compiled into structured records capturing displaced\
    \ population counts and characteristics in post-event shelter settings."
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/peru-dtmr3
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Displaced population in shelters following flood displacement in
      Piura districts
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Sample Survey
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: In this file, we show dataset of the third (3rd) round of Displacement
    Tracking Matrix (DTM) in Piura, Peru; wich was done between 17th June and 16th
    July,
  download_url: https://data.humdata.org/dataset/dad01c41-adde-46ee-998d-a6baf9eeb8d1/resource/538975d3-f7bb-4f0d-9111-58f7e00ee4f1/download/dtm3_version_publica_1209-1.xlsx
  format: null
  id: resource_538975d3
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM3 PERU.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: PERU - Displacement Tracking Matrix (Round 3) (DTM3 PERU Survey.pdf)
  download_url: https://data.humdata.org/dataset/dad01c41-adde-46ee-998d-a6baf9eeb8d1/resource/059f4769-6b33-4fdd-ae15-8ec05547613e/download/oim-cuestionario_dtm-r3-12092017.pdf
  format: null
  id: resource_059f4769
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM3 PERU Survey.pdf
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-per_iom_displacementtrackingmatri_2017
spatial:
  bbox: null
  centroid: null
  countries:
  - PER
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2017-07-17'
  start: '2017-06-16'
temporal_resolution: null
title: PERU - Displacement Tracking Matrix (Round 3)
version: null
vulnerability: null
---
