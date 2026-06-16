---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap
    url: https://data.humdata.org/dataset/central-america-water-bodies-percentage-by-ach-gis4tech
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: "Acci\xF3n contra el hambre - GIS4tech"
  url: https://data.humdata.org/dataset/central-america-water-bodies-percentage-by-ach-gis4tech
creator:
  affiliation: null
  email: null
  name: "Acci\xF3n contra el hambre - GIS4tech"
  url: https://data.humdata.org/dataset/central-america-water-bodies-percentage-by-ach-gis4tech
dataset_id: rdls_exp-achgis4tech_centralamericawaterbodies_2020
description: 'Percentage of areas covered by bodies of water that are found on the
  land surface or in the subsoil, whether natural or artificial, and may be fresh,
  brackish or salt water. Data source: OpenStreetMap. For more information contact
  GIS4Tech: info@gis4tech.com. You can also visit the PREDISAN platform https://predisan.gis4tech.com/ca4
  for detailed, accurate information.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/central-america-water-bodies-percentage-by-ach-gis4tech]'
details: null
exposure:
- asset_type:
    description: Percentage coverage of water bodies (natural and artificial) at municipal
      scale across Central America
    id: natural_environment
    scheme: null
    title: null
    uri: null
  category: natural_environment
  id: exposure_1
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
hazard: null
license: CC-BY-4.0
lineage:
  description: Water body features were extracted from OpenStreetMap and processed
    using GIS geoprocessing techniques to calculate the percentage coverage of water
    bodies (fresh, brackish, and salt water) at the municipal scale across Central
    America. Post-processing aggregation transformed the data from feature-level to
    administrative unit (municipality) scale.
  sources:
  - id: source_1
    license: null
    name: OpenStreetMap
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/central-america-water-bodies-percentage-by-ach-gis4tech
  rel: source
loss: null
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
  description: Central America water bodies percentage by ACH-GIS4Tech (Percentage
    of areas covered by water bodies in Central America.)
  download_url: https://data.humdata.org/dataset/2f73d279-8374-43cd-ba6b-cff81ece3269/resource/02467b8d-2d4c-43ac-8e21-0e7138d0d48a/download/area_water_bodies.csv
  format: null
  id: resource_02467b8d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2020 Central America water bodies by ACH-GIS4Tech.csv
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-achgis4tech_centralamericawaterbodies_2020
spatial:
  bbox: null
  centroid: null
  countries:
  - GTM
  - BLZ
  - SLV
  - HND
  - NIC
  - CRI
  - PAN
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-12-31'
  start: '2020-01-01'
temporal_resolution: null
title: Central America water bodies percentage by ACH-GIS4Tech
version: null
vulnerability: null
---
