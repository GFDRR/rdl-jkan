---
attributions:
- entity:
    affiliation: null
    email: null
    name: IBTrACS (International Best Track Archive for Climate Stewardship)
    url: https://data.humdata.org/dataset/central-america-storm-and-hurricane-risk
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: "Acci\xF3n contra el hambre - GIS4tech"
  url: https://data.humdata.org/dataset/central-america-storm-and-hurricane-risk
creator:
  affiliation: null
  email: null
  name: "Acci\xF3n contra el hambre - GIS4tech"
  url: https://data.humdata.org/dataset/central-america-storm-and-hurricane-risk
dataset_id: rdls_hzd-gtmhndnicslv_achgis4tech_centralamericastormhurric_2019
description: 'Storm and hurricane risk has been assessed based on a database called
  IBTrACS obtained from the NOAA (National Centers for Environmental Information).
  The hazard classification is determined by the frequency of the events. The information
  is showed by country, department and municipality of Central America (Nicaragua,
  Honduras, Guatemala, El Salvador) For more information contact GIS4Tech: info@gis4tech.com.
  You can also visit the PREDISAN platform https://predisan.gis4tech.com/ca4 for detailed,
  accurate information.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/central-america-storm-and-hurricane-risk]'
details: null
exposure: []
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: inferred
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-4.0
lineage:
  description: Historical storm and hurricane events were extracted from the IBTrACS
    database maintained by NOAA. Event frequency per municipality was calculated and
    categorized into four risk levels (low, medium, high, very high) based on the
    number of registered events. Risk classifications were assigned to administrative
    units (country, department, municipality) across Central America.
  sources:
  - id: source_1
    license: null
    name: IBTrACS (International Best Track Archive for Climate Stewardship)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/central-america-storm-and-hurricane-risk
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
  description: Central America - Storm and Hurricane Risk (Storm and hurricane risk
    in Central America)
  download_url: https://data.humdata.org/dataset/17fbd26e-3bba-46ac-a63f-ab95c2b5afe2/resource/edf4c3fb-0593-4140-84b5-0fe3410138da/download/storm_and_hurricane_risk.csv
  format: null
  id: resource_edf4c3fb
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: storm_and_hurricane_risk.csv
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-gtmhndnicslv_achgis4tech_centralamericastormhurric_2019
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
  end: '2019-12-31'
  start: '2019-01-01'
temporal_resolution: null
title: Central America - Storm and Hurricane Risk
version: null
vulnerability: null
---
