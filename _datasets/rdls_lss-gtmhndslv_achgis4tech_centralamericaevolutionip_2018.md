---
attributions:
- entity:
    affiliation: null
    email: null
    name: Integrated Food Security Phase Classification (IPC)
    url: https://data.humdata.org/dataset/central-america-evolution-of-the-ipc
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: "Acci\xF3n contra el hambre - GIS4tech"
  url: https://data.humdata.org/dataset/central-america-evolution-of-the-ipc
creator:
  affiliation: null
  email: null
  name: "Acci\xF3n contra el hambre - GIS4tech"
  url: https://data.humdata.org/dataset/central-america-evolution-of-the-ipc
dataset_id: rdls_lss-gtmhndslv_achgis4tech_centralamericaevolutionip_2018
description: 'The dataset displays the Integrated Food Security Phase Classification
  (IPC), a standardized global scale used to measure the severity and magnitude of
  food insecurity and malnutrition. The data, compared with a five-year historical
  series for the countries of El Salvador, Guatemala, and Honduras, have been assessed
  based on information obtained from the IPC portal. For more information contact
  GIS4Tech: info@gis4tech.com. You can also visit the PREDISAN platform https://predisan.gis4tech.com/ca4
  for detailed, accurate information.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/central-america-evolution-of-the-ipc]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: IPC classification documents were obtained from the IPC portal, scraped
    for relevant information, standardized, and loaded into tabular format with population
    estimates and phase distribution percentages across administrative divisions in
    El Salvador, Guatemala, and Honduras over a five-year historical series.
  sources:
  - id: source_1
    license: null
    name: Integrated Food Security Phase Classification (IPC)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/central-america-evolution-of-the-ipc
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Food insecurity phase classification affecting population in Central
      America
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
  description: Central America - Evolution of the IPC (Evolution of the IPC by ACH-GIS4Tech.csv)
  download_url: https://data.humdata.org/dataset/9d01fed3-74b6-490f-a035-1a9d43c65b2a/resource/7723f7ed-42e2-4c8f-bdc3-be8c9708702d/download/evolution_of_the-_ipc.csv
  format: null
  id: resource_7723f7ed
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: evolution_of_the _IPC.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-gtmhndslv_achgis4tech_centralamericaevolutionip_2018
spatial:
  bbox: null
  centroid: null
  countries:
  - SLV
  - GTM
  - HND
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-05-01'
  start: '2018-12-01'
temporal_resolution: null
title: Central America - Evolution of the IPC
version: null
vulnerability: null
---
