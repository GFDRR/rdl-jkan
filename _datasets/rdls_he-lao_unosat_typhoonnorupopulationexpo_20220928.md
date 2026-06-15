---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/unosat-typhoon-noru-population-exposure-analysis-in-lao-people-s-democratic-republic-28-se
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-typhoon-noru-population-exposure-analysis-in-lao-people-s-democratic-republic-28-se
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-typhoon-noru-population-exposure-analysis-in-lao-people-s-democratic-republic-28-se
dataset_id: rdls_he-lao_unosat_typhoonnorupopulationexpo_20220928
description: 'UNOSAT code TC20220928LAO, GDACS Id: 1000922 Typhoon Noru originated
  from a disturbance over the Philippine Sea. The storm made its first landfall over
  the Polillo Islands, Philippines on September 26 at 09:30 UTC and its second over
  Central Luzon five hours later as a high-end typhoon. The storm also made the third
  landfall in the early morning of 28 Sep 22 with winds of 117 km/h in the province
  of Quang Nam, home to the historic city of Hoi An and resort of Danang of Viet Nam.
  Typhoon Noru is expected to hit the central and southern provinces of Lao PDR on
  Wednesday, bringing heavy rain and thunderstorm to most of the country. According
  to GDACS, Typhoon Noru can have a high humanitarian impact based on the maximum
  sustained wind speed, exposed population, and vulnerability. Based on data of the
  forecasted the cyclone path of wind speeds zones from Joint Research Centre (Issued
  on 28 September 2022 at 07:00 local time), and population data from WorldPop 2020,
  UNITAR-UNOSAT has prepared a population exposure analysis for Lao PDR. About 2%
  of population of Lao PDR living inside wind speed zone exceed 120 km/h, 16% living
  inside wind speed zone of 60-120 km/h and 20% living inside wind speed zone below
  60 km/h. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/unosat-typhoon-noru-population-exposure-analysis-in-lao-people-s-democratic-republic-28-se]'
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
    description: Population exposed to Typhoon NORU in Lao PDR provinces
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
    - analysis_type: probabilistic
      calculation_method: observed
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
  description: UNOSAT analysts reviewed satellite imagery to identify the typhoon
    track and affected areas in Lao PDR, then intersected the hazard zone with gridded
    population data to quantify population exposure to tropical cyclone winds from
    Typhoon NORU on 28 September 2022.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/unosat-typhoon-noru-population-exposure-analysis-in-lao-people-s-democratic-republic-28-se
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
  description: UNOSAT Typhoon NORU Population Exposure Analysis in Lao People's Democratic
    Republic 28 September 2022 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3381/UNOSAT_PopulationExposureAnalysis_TropicalCycloneNORU_LaoPDR_28Sep2022.xlsx
  format: null
  id: resource_aaf709e3
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_PopulationExposureAnalysis_TropicalCycloneNORU_LaoPDR_28Sep2022.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-lao_unosat_typhoonnorupopulationexpo_20220928
spatial:
  bbox: null
  centroid: null
  countries:
  - LAO
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-09-28'
temporal_resolution: null
title: UNOSAT Typhoon NORU Population Exposure Analysis in Lao People's Democratic
  Republic 28 September 2022
version: null
vulnerability: null
---
