---
attributions:
- entity:
    affiliation: null
    email: null
    name: Joint Research Centre (JRC)
    url: https://data.humdata.org/dataset/tropical-storm-kenneth-population-exposure-analysis-in-mozambique-23-april-2019
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop 2015
    url: https://data.humdata.org/dataset/tropical-storm-kenneth-population-exposure-analysis-in-mozambique-23-april-2019
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/tropical-storm-kenneth-population-exposure-analysis-in-mozambique-23-april-2019
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/tropical-storm-kenneth-population-exposure-analysis-in-mozambique-23-april-2019
dataset_id: rdls_he-moz_unosat_cyclonekennethpopulatione_20190423
description: 'Just over a month after the tropical cyclone IDAI-19 a new tropical
  storm is heading toward Comoros, Tanzania and the north of Mozambique called ''twentyfour-19''.
  The category 2 tropical storm is expected to make landfall between the 27th and
  the 28th of April 2018 south of Mocimboa da Praia town located in the province of
  Cabo Delgado in the extreme northern part of Mozambique. Based on data of the expected
  tropical cyclone path Twentyfour-19, wind speeds zones from Joint Research Centre
  (Issued on 23 April 2019 06:00 UTC), and population data from WorldPop 2015, UNITAR-UNOSAT
  conducted a population exposure analysis for Mozambique. About 750,000 people in
  Mozambique, mainly in Cabo Delgado province are living inside the wind speed zones
  of 120 km/h, 90 km/h and 60 km/h accordingly. Cyclone track: Joint Research Centre
  (JRC) as of 23/04/2019 Wind speed zones: Joint Research Centre (JRC) as of 23/04/2019,
  06:00 UTC Administrative Levels: OCHA ROSEA Spatial Demographic Data: WorldPop (2015),
  100m spatial resolution Analysis: UNITAR-UNOSAT (23/04/2019). [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/tropical-storm-kenneth-population-exposure-analysis-in-mozambique-23-april-2019]'
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
    description: Residential population exposed to tropical cyclone wind speeds from
      WorldPop 2015
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
  event_sets:
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: JRC tropical cyclone wind speed forecast model (issued 23 April 2019)
    was intersected with WorldPop 2015 gridded population data to quantify population
    exposure to predicted wind speed zones from Cyclone Kenneth landfall in Cabo Delgado
    province, northern Mozambique.
  sources:
  - id: source_1
    license: null
    name: Joint Research Centre (JRC)
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: WorldPop 2015
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/tropical-storm-kenneth-population-exposure-analysis-in-mozambique-23-april-2019
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Cyclone Kenneth: Population Exposure Analysis in Mozambique - 23 April
    2019 (Excel)'
  download_url: https://data.humdata.org/dataset/d607761b-c9f9-437d-8480-105adad64283/resource/6dce96b6-2469-40d2-9abf-fcbbd8e24d09/download/unosat_population_exposure_twentyfour19.xlsx
  format: null
  id: resource_6dce96b6
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_population_exposure_twentyfour19.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-moz_unosat_cyclonekennethpopulatione_20190423
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
  start: '2019-04-23'
temporal_resolution: null
title: 'Cyclone Kenneth: Population Exposure Analysis in Mozambique - 23 April 2019'
version: null
vulnerability: null
---
