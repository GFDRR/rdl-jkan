---
attributions:
- entity:
    affiliation: null
    email: null
    name: European Commission Joint Research Centre
    url: https://data.humdata.org/dataset/central-america-flood-risk
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: "Acci\xF3n contra el hambre - GIS4tech"
  url: https://data.humdata.org/dataset/central-america-flood-risk
creator:
  affiliation: null
  email: null
  name: "Acci\xF3n contra el hambre - GIS4tech"
  url: https://data.humdata.org/dataset/central-america-flood-risk
dataset_id: rdls_he-gtmhndnicslv_achgis4tech_centralamericafloodrisk_2016
description: 'Flood risk has been assessed based on data obtained from European Commission''s
  Joint Research Centre. In this analysis, the amount of surface for each municipality
  that is in flood risk areas has been compiled. The hazard classification is determined
  using Jenks Natural Breaks Classification (or Optimization) system. The information
  is showed by country, department and municipality of Central America (Nicaragua,
  Honduras, Guatemala, El Salvador). For more information contact GIS4Tech: info@gis4tech.com.
  You can also visit the PREDISAN platform https://predisan.gis4tech.com/ca4 for detailed,
  accurate information.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/central-america-flood-risk]'
details: null
exposure:
- asset_type:
    description: Municipal surface area classified by flood risk category
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
hazard:
  event_sets_by_hazard_type:
    flood:
    - analysis_type: deterministic
      calculation_method: inferred
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Flood hazard data from the European Commission's Joint Research Centre
    was obtained and processed to calculate the surface area in flood risk zones for
    each municipality across Central America. Municipal-level flood risk areas were
    classified using Jenks Natural Breaks Optimization, with municipalities having
    zero flood hazard records assigned to the 'Low' category and remaining municipalities
    distributed across medium, high, and very high risk classes.
  sources:
  - id: source_1
    license: null
    name: European Commission Joint Research Centre
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/central-america-flood-risk
  rel: source
loss:
  losses: []
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
  description: Central America - Flood risk (Flood risk)
  download_url: https://data.humdata.org/dataset/75b4d2a3-80ec-4a81-b066-bfc890ac40e2/resource/39aa7d81-9e25-4fa2-a3ed-79366d4abd4f/download/flood_risk.csv
  format: null
  id: resource_39aa7d81
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: flood_risk.csv
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-gtmhndnicslv_achgis4tech_centralamericafloodrisk_2016
spatial:
  bbox: null
  centroid: null
  countries:
  - NIC
  - HND
  - GTM
  - SLV
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2016-12-31'
  start: '2016-01-01'
temporal_resolution: null
title: Central America - Flood risk
version: null
vulnerability: null
---
