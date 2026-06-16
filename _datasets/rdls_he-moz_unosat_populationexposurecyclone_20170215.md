---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/population-exposure-cyclone-dineo-17-mozambique
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/population-exposure-cyclone-dineo-17-mozambique
dataset_id: rdls_he-moz_unosat_populationexposurecyclone_20170215
description: 'The Tropical Cyclone Dineo-17, is approaching Mozambique coasts and
  is expected to make landfall The 16 February 2017 in the central province of Inhambane.
  Potential heavy rainfall are also expected according microwave satellite sensors
  and might induce flooding in the affected areas. This report provides an analysis
  on the potentially exposed population per wind speed zones in Mozambique. According
  to our analysis approximately 250,000 people in Mozambique may be exposed to over
  120km/h sustainable wind speeds and 59,000 people might be exposed to 90km/h wind
  speed. About 1,160,000 people might be exposed to moderate winds of 60km/h.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/population-exposure-cyclone-dineo-17-mozambique]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure:
- asset_type:
    description: Population exposed to tropical cyclone wind speed zones in Mozambique
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard:
  event_sets_by_hazard_type:
    strong_wind:
    - analysis_type: deterministic
      calculation_method: simulated
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
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts reviewed satellite imagery from Tropical Cyclone Dineo-17
    to delineate wind speed hazard zones across Mozambique. Gridded population data
    was intersected with wind speed zones (90 km/h and 120 km/h thresholds) to estimate
    population exposure per wind speed category, producing a deterministic exposure
    assessment for the approaching cyclone event.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/population-exposure-cyclone-dineo-17-mozambique
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
  description: Mozambique - Population Exposure-Cyclone Dineo-17 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MZ/FL20170118MOZ/UNOSAT_Pop_exposure_dineo17_20170215.xlsx
  format: null
  id: resource_e82c7420
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_Pop_exposure_dineo17_20170215.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-moz_unosat_populationexposurecyclone_20170215
spatial:
  bbox: null
  centroid: null
  countries:
  - MOZ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-02-15'
temporal_resolution: null
title: Mozambique - Population Exposure-Cyclone Dineo-17
version: null
vulnerability: null
---
