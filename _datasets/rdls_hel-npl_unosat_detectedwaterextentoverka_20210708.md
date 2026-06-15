---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-2 satellite imagery
    url: https://data.humdata.org/dataset/water-extent-over-kaski-and-syangja-districts-gandaki-province-nepal-as-of-4-july-2021
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population data
    url: https://data.humdata.org/dataset/water-extent-over-kaski-and-syangja-districts-gandaki-province-nepal-as-of-4-july-2021
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-kaski-and-syangja-districts-gandaki-province-nepal-as-of-4-july-2021
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-kaski-and-syangja-districts-gandaki-province-nepal-as-of-4-july-2021
dataset_id: rdls_hel-npl_unosat_detectedwaterextentoverka_20210708
description: 'UNOSAT code: FL20210630NPL This map illustrates satellite-detected surface
  waters in Kaski and Syangja districts, Gandaki province, Nepal as observed from
  a Sentinel-2 image acquired on 4 July 2021 at 10:41 local time. Within the analyzed
  cloud free zones of about 500 km2, a total of about 25km2 of lands appear to be
  flooded. Based on Worldpop population data and the detected surface waters, about
  17,000 people are potentially exposed or living close to flooded areas. The potentially
  exposed population is mainly located in the Kaski district with ~16,000 people.
  This is a preliminary analysis and has not yet been validated in the field. Please
  send ground feedback to United Nations Satellite Centre (UNOSAT).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-over-kaski-and-syangja-districts-gandaki-province-nepal-as-of-4-july-2021]'
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
    description: Population potentially exposed or living close to satellite-detected
      flooded areas based on WorldPop data
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
    flood:
    - analysis_type: empirical
      calculation_method: observed
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "UNOSAT analysts reviewed Sentinel-2 satellite imagery acquired on\
    \ 4 July 2021 to detect surface water extent through visual comparison and change\
    \ detection methods. Detected flooded areas (~25 km\xC2\xB2) were intersected\
    \ with WorldPop gridded population data to estimate approximately 17,000 people\
    \ potentially exposed to flooding in Kaski and Syangja districts."
  sources:
  - id: source_1
    license: null
    name: Sentinel-2 satellite imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: WorldPop population data
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/water-extent-over-kaski-and-syangja-districts-gandaki-province-nepal-as-of-4-july-2021
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population potentially exposed to flooded areas as of 4 July 2021
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: direct
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
  description: Satellite detected water extent over Kaski and Syangja districts, Gandaki
    province, Nepal as of 4 July 2021 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/NP/FL20210630NPL/FL20210630NPL_gdb.zip
  format: Geodatabase
  id: resource_88df6ce1
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20210630NPL_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent over Kaski and Syangja districts, Gandaki
    province, Nepal as of 4 July 2021 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/NP/FL20210630NPL/FL20210630NPL_SHP.zip
  format: null
  id: resource_1d785915
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20210630NPL_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-npl_unosat_detectedwaterextentoverka_20210708
spatial:
  bbox: null
  centroid: null
  countries:
  - NPL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-07-08'
temporal_resolution: null
title: Satellite detected water extent over Kaski and Syangja districts, Gandaki province,
  Nepal as of 4 July 2021
version: null
vulnerability: null
---
