---
attributions:
- entity:
    affiliation: null
    email: null
    name: Ministry of Environment of El Salvador
    url: https://data.humdata.org/dataset/volcanic-activity-risk-in-central-america
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: "Acci\xF3n contra el hambre - GIS4tech"
  url: https://data.humdata.org/dataset/volcanic-activity-risk-in-central-america
creator:
  affiliation: null
  email: null
  name: "Acci\xF3n contra el hambre - GIS4tech"
  url: https://data.humdata.org/dataset/volcanic-activity-risk-in-central-america
dataset_id: rdls_hzd-gtmhndnicslv_achgis4tech_centralamericavolcanicact_2016
description: 'Volcanic activity risk has been assessed based on data obtained from
  the Ministry of Environment of El Salvador. In this analysis, circular areas have
  been delineated around the location of each active volcano. The hazard classification
  is determined by the proximity of a specific area to a volcano. The information
  is showed by country, department and municipality of Central America (Nicaragua,
  Honduras, Guatemala, El Salvador) For more information contact GIS4Tech: info@gis4tech.com.
  You can also visit the PREDISAN platform https://predisan.gis4tech.com/ca4 for detailed,
  accurate information.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/volcanic-activity-risk-in-central-america]'
details: null
exposure: []
hazard:
  event_sets_by_hazard_type:
    volcanic:
    - analysis_type: deterministic
      calculation_method: inferred
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: h_vaf:mm
        process: ashfall
        trigger: null
        type: volcanic
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Active volcano locations from El Salvador's Ministry of Environment
    were used to delineate circular hazard zones around each volcano. Volcanic risk
    levels (0-3) were assigned to administrative units (municipalities) based on maximum
    proximity to volcanoes, with level 0 indicating no volcanic danger and levels
    1-3 indicating increasing risk. The dataset aggregates this classification across
    four Central American countries at the municipality level.
  sources:
  - id: source_1
    license: null
    name: Ministry of Environment of El Salvador
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/volcanic-activity-risk-in-central-america
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
  description: Central America - Volcanic activity risk (Volcanic activity risk in
    Central America)
  download_url: https://data.humdata.org/dataset/dc2c25fe-8ab3-4d24-a0f9-da85a93ef15a/resource/85f49572-b83e-4d44-affe-9880b2f248b2/download/volcanic_activity_risk.csv
  format: null
  id: resource_85f49572
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Volcanic activity risk in Central America (Nicaragua, Honduras, Guatemala,
    El Salvador)
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-gtmhndnicslv_achgis4tech_centralamericavolcanicact_2016
spatial:
  bbox: null
  centroid: null
  countries:
  - SLV
  - HND
  - GTM
  - NIC
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2016-12-31'
  start: '2016-01-01'
temporal_resolution: null
title: Central America - Volcanic activity risk
version: null
vulnerability: null
---
