---
attributions:
- entity:
    affiliation: null
    email: null
    name: Joint Typhoon Warning Center (JTWC)
    url: https://data.humdata.org/dataset/tropical-cyclone-yagi-impact-assessment-to-strong-wind-as-of-7-september-2024
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/tropical-cyclone-yagi-impact-assessment-to-strong-wind-as-of-7-september-2024
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/tropical-cyclone-yagi-impact-assessment-to-strong-wind-as-of-7-september-2024
dataset_id: rdls_hel-vnm_unosat_tropicalcycloneyagiimpact_20240908
description: 'UNOSAT code: TC20240905VNM, GDACS ID: 1001090 This map illustrates the
  tropical cyclone paths of YAGI in Viet Nam, highlighting observed and predicted
  wind speed zones between 1 and 9 September 2024. According to the data from the
  Joint Typhoon Warning Center (JTWC), as of 7 September 2024 at 06:00 UTC, approximately
  23 million people (24% of the total population) live within areas where wind speeds
  exceed 120 km/h. Notably, in Ha Noi Province, around 8.2 million people have been
  affected by strong winds. This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to the United Nations Satellite Centre
  (UNOSAT).. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/tropical-cyclone-yagi-impact-assessment-to-strong-wind-as-of-7-september-2024]'
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
    description: Population exposed to strong wind speeds exceeding 120 km/h from
      tropical cyclone YAGI
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
  description: UNOSAT analysts reviewed satellite imagery and JTWC tropical cyclone
    track and wind speed data to map observed and predicted wind speed zones from
    Typhoon YAGI across Vietnam. Population exposure analysis was conducted by intersecting
    wind speed zones with gridded population data to quantify affected populations
    by province and nationally.
  sources:
  - id: source_1
    license: null
    name: Joint Typhoon Warning Center (JTWC)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/tropical-cyclone-yagi-impact-assessment-to-strong-wind-as-of-7-september-2024
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by strong winds exceeding 120 km/h from tropical
      cyclone YAGI
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: inferred
        type: direct
      loss_approach: analytical
      loss_frequency_type: deterministic
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
  description: 'Viet Nam - Tropical Cyclone YAGI: Impact assessment to strong wind
    as of 7 September 2024 (Excel file)'
  download_url: https://unosat.org/static/unosat_filesystem/3955/UNOSAT_PopulationExposureAnalysis_TC_YAGI_VIETNAM_07SEP2024_0600UTC.xlsx
  format: null
  id: resource_43ab5ab4
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_PopulationExposureAnalysis_TC_YAGI_VIETNAM_07SEP2024_0600UTC.xlsx
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-vnm_unosat_tropicalcycloneyagiimpact_20240908
spatial:
  bbox: null
  centroid: null
  countries:
  - VNM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-09-08'
temporal_resolution: null
title: 'Viet Nam - Tropical Cyclone YAGI: Impact assessment to strong wind as of 7
  September 2024'
version: null
vulnerability: null
---
