---
attributions:
- entity:
    affiliation: null
    email: null
    name: GeoEye-1 satellite imagery
    url: https://data.humdata.org/dataset/flood-impact-assessment-of-mueang-ubon-ratchathani-warin-chamrap-and-sawang-wirawong-distr
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population data
    url: https://data.humdata.org/dataset/flood-impact-assessment-of-mueang-ubon-ratchathani-warin-chamrap-and-sawang-wirawong-distr
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/flood-impact-assessment-of-mueang-ubon-ratchathani-warin-chamrap-and-sawang-wirawong-distr
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/flood-impact-assessment-of-mueang-ubon-ratchathani-warin-chamrap-and-sawang-wirawong-distr
dataset_id: rdls_hel-tha_unosat_floodimpactassessmentmuea_20221103
description: "UNOSAT code TC20220928THA, GDACS Id: 1000922 This map illustrates satellite-detected\
  \ surface waters in Ubon Ratchathani Province, Thailand as observed from a GeoEye-1\
  \ image acquired on 20 October 2022 at 10:35 local time. Within the analysis extent\
  \ of this map, about 120 km\xB2 of lands appear to be flooded. Based on Worldpop\
  \ population data and the detected surface waters within the analysis extent, approximately\
  \ 32,000 people are potentially exposed to or living close to flooded areas along\
  \ with 11,330 structures and approximately 400 km roads potentially damaged by flooding.\
  \ This is a preliminary analysis and has not yet been validated in the field. Please\
  \ send ground feedback to United Nations Satellite Centre (UNOSAT).. [Source: This\
  \ metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/flood-impact-assessment-of-mueang-ubon-ratchathani-warin-chamrap-and-sawang-wirawong-distr]"
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
    description: Population potentially exposed to or living close to flooded areas
      based on WorldPop data
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
- asset_type:
    description: Building structures potentially damaged by flooding in the analysis
      extent
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Road network potentially damaged by flooding
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_3
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: length
      unit: null
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
  description: "UNOSAT analysts interpreted GeoEye-1 satellite imagery acquired on\
    \ 20 October 2022 to detect surface water extent covering approximately 120 km\xB2\
    \ in Ubon Ratchathani Province. Detected flooded areas were overlaid with WorldPop\
    \ population grids and building footprint/structure inventories to estimate exposure\
    \ (32,000 people, 11,330 structures) and infrastructure at risk (400 km of roads).\
    \ Results were compiled into geodatabase and shapefile formats with impact metrics."
  sources:
  - id: source_1
    license: null
    name: GeoEye-1 satellite imagery
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
- href: https://data.humdata.org/dataset/flood-impact-assessment-of-mueang-ubon-ratchathani-warin-chamrap-and-sawang-wirawong-distr
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population potentially exposed to flooded areas
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
  - asset_category: buildings
    asset_dimension: structure
    description: Building structures potentially damaged by flooding
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: Road infrastructure potentially damaged by flooding
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_3
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
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
  description: Flood Impact assessment of Mueang Ubon Ratchathani, Warin Chamrap,
    and Sawang Wirawong Districts, Ubon Ratchathani Province, Thailand as of 20 October
    2022 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3433/TC20220928THA_gdb.zip
  format: Geodatabase
  id: resource_f6251c0a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20220928THA_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flood Impact assessment of Mueang Ubon Ratchathani, Warin Chamrap,
    and Sawang Wirawong Districts, Ubon Ratchathani Province, Thailand as of 20 October
    2022 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3433/TC20220928THA_SHP.zip
  format: null
  id: resource_f1b57950
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20220928THA_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flood Impact assessment of Mueang Ubon Ratchathani, Warin Chamrap,
    and Sawang Wirawong Districts, Ubon Ratchathani Province, Thailand as of 20 October
    2022 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3433/UNOSAT_Population_Exposure_TC20220928THA_UbonRatchathani_Thailand20Oct2022.xlsx
  format: null
  id: resource_78249513
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_Population_Exposure_TC20220928THA_UbonRatchathani_Thailand20Oct2022.xlsx
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-tha_unosat_floodimpactassessmentmuea_20221103
spatial:
  bbox: null
  centroid: null
  countries:
  - THA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-11-03'
temporal_resolution: null
title: Flood Impact assessment of Mueang Ubon Ratchathani, Warin Chamrap, and Sawang
  Wirawong Districts, Ubon Ratchathani Province, Thailand as of 20 October 2022
version: null
vulnerability: null
---
