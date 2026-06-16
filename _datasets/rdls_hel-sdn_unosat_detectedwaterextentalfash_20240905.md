---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extent-in-al-fashir-city-al-fasher-department-al-fasher-state-sudan-as-of-3-septembe
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-al-fashir-city-al-fasher-department-al-fasher-state-sudan-as-of-3-septembe
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-al-fashir-city-al-fasher-department-al-fasher-state-sudan-as-of-3-septembe
dataset_id: rdls_hel-sdn_unosat_detectedwaterextentalfash_20240905
description: "UNOSAT code: FL20240826SDN, GDACS ID: 1102854 This map illustrates satellite-detected\
  \ water extent in Al Fashir City, Al Fasher Department, Al Fasher State, Sudan as\
  \ observed from a WorldView-2 satellite image acquired on 3 September 2024 at 10:43\
  \ local time (08:43 UTC). Within analysed area of about 270km\xB2, a total of about\
  \ 100 km\xB2 of land appears to be affected by floodwaters. UNITAR-UNOSAT identified\
  \ about 1,600 potentially affected structures within the analysed area. This is\
  \ a preliminary analysis and has not yet been validated in the field. Please send\
  \ ground feedback to the United Nations Satellite Centre (UNOSAT). [Source: This\
  \ metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-in-al-fashir-city-al-fasher-department-al-fasher-state-sudan-as-of-3-septembe]"
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
    description: Building structures identified within the analyzed area of Al Fashir
      City
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
  description: "UNOSAT analysts processed WorldView-2 satellite imagery acquired on\
    \ 3 September 2024 over Al Fashir City, comparing multi-temporal images to detect\
    \ changes in water extent and identify potentially affected structures. The analysis\
    \ delineated approximately 100 km\xB2 of floodwaters within a 270 km\xB2 study\
    \ area and mapped 1,600 potentially affected building structures."
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/water-extent-in-al-fashir-city-al-fasher-department-al-fasher-state-sudan-as-of-3-septembe
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Potentially affected structures identified within satellite-detected
      flood extent
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
  description: Satellite detected water extent in Al Fashir City, Al Fasher Department,
    Al Fasher State, Sudan as of 3 September 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3948/FL20240826SDN_gdb.zip
  format: Geodatabase
  id: resource_f260b18e
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240826SDN_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent in Al Fashir City, Al Fasher Department,
    Al Fasher State, Sudan as of 3 September 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3948/FL20240826SDN_SHP.zip
  format: null
  id: resource_94ba7a44
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240826SDN_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-sdn_unosat_detectedwaterextentalfash_20240905
spatial:
  bbox: null
  centroid: null
  countries:
  - SDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-09-05'
temporal_resolution: null
title: Satellite detected water extent in Al Fashir City, Al Fasher Department, Al
  Fasher State, Sudan as of 3 September 2024
version: null
vulnerability: null
---
