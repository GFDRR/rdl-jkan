---
attributions:
- entity:
    affiliation: null
    email: null
    name: Humanitarian partners
    url: https://data.humdata.org/dataset/colombia-people-in-need-pin-del-cluster-en-seguridad-alimentaria-y-nutricion-san-sp
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/colombia-people-in-need-pin-del-cluster-en-seguridad-alimentaria-y-nutricion-san-sp
creator:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/colombia-people-in-need-pin-del-cluster-en-seguridad-alimentaria-y-nutricion-san-sp
dataset_id: rdls_lss-col_ochacol_peopleneedpindelclusteren_2022
description: "Esta base de datos contiene los c\xE1lculos de People in Need (PiN)\
  \ del Cl\xFAster de Seguridad Alimentaria y Nutrici\xF3n realizados en el marco\
  \ del Ciclo de Programaci\xF3n Humanitaria de Colombia para 2023. El PiN se calcula\
  \ a partir de la informaci\xF3n disponible del % de poblaci\xF3n en inseguridad\
  \ alimentaria y de las prevalencias de desnutrici\xF3n aguda y bajo peso al nacer.\
  \ En la estimaci\xF3n, se prioriza una parte de la poblaci\xF3n con inseguridad\
  \ alimentaria moderada y la totalidad de la severa en las zonas del pa\xEDs en donde\
  \ se reportan las mayores brechas poblacionales y de acceso. La poblaci\xF3n con\
  \ necesidades en SAN es menor que el % de poblaci\xF3n en inseguridad alimentaria\
  \ y de desnutrici\xF3n aguda/bajo peso.. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/colombia-people-in-need-pin-del-cluster-en-seguridad-alimentaria-y-nutricion-san-sp]"
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: People in Need estimates were calculated from aggregated humanitarian
    partner data on food insecurity prevalence (moderate and severe) and acute malnutrition/low
    birth weight prevalence across Colombia. Prioritization was applied to moderate
    food insecurity populations and all severe cases in areas with the largest population
    gaps and access constraints, generating national-level humanitarian needs assessments
    for the 2023 programming cycle.
  sources:
  - id: source_1
    license: null
    name: Humanitarian partners
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/colombia-people-in-need-pin-del-cluster-en-seguridad-alimentaria-y-nutricion-san-sp
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population in need due to food insecurity and malnutrition from drought-related
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
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Colombia: People in Need (PiN) del Cl\xFAster en Seguridad Alimentaria\
    \ y Nutrici\xF3n (SAN-SP)"
  download_url: https://data.humdata.org/dataset/7d891bdf-6e9e-46cc-896a-746489f5e39e/resource/c17c4113-b885-4799-b24a-44562eb57947/download/pin_seguridad-alimentaria-y-nutricion_2023_hdx.xlsx
  format: null
  id: resource_c17c4113
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "PiN_Seguridad Alimentaria y Nutrici\xF3n_2023.xlsx"
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-col_ochacol_peopleneedpindelclusteren_2022
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
  end: '2022-12-31'
  start: '2022-01-01'
temporal_resolution: null
title: "Colombia: People in Need (PiN) del Cl\xFAster en Seguridad Alimentaria y Nutrici\xF3\
  n (SAN-SP)"
version: null
vulnerability: null
---
