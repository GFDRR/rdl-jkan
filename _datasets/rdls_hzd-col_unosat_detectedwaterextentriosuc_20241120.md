---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extent-in-riosucio-municipality-choco-department-colombia-as-of-17-november-2024
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-riosucio-municipality-choco-department-colombia-as-of-17-november-2024
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-riosucio-municipality-choco-department-colombia-as-of-17-november-2024
dataset_id: rdls_hzd-col_unosat_detectedwaterextentriosuc_20241120
description: "UNOSAT code: FL20241112COL, GDACS ID: 1102988 This map illustrates satellite-detected\
  \ water extent in Riosucio Municipality, Choc\xF3 Department, Colombia as observed\
  \ from a TanDEM-X radar image acquired on the 17 November 2024. Within the analysed\
  \ area of about 1,130km\xB2, a total of about 12 km\xB2 of lands appear to be affected\
  \ with flood waters. This is a preliminary analysis and has not yet been validated\
  \ in the field. Please send ground feedback to the United Nations Satellite Centre\
  \ (UNOSAT). Important note: Flood analysis based on radar images may underestimate\
  \ the extent of standing water in built-up or densely vegetated areas due to the\
  \ radar signal's backscattering properties.. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-in-riosucio-municipality-choco-department-colombia-as-of-17-november-2024]"
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure: []
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
        intensity_measure: AA:km2
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "TanDEM-X radar imagery acquired on 17 November 2024 was analyzed by\
    \ UNOSAT analysts through multi-temporal comparison with reference imagery to\
    \ detect notable changes in water extent. Satellite-detected inundated areas were\
    \ delineated and quantified as approximately 12 km\xB2 within the 1,130 km\xB2\
    \ study area of Riosucio Municipality. This is a preliminary post-event empirical\
    \ hazard assessment not yet validated in the field."
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
- href: https://data.humdata.org/dataset/water-extent-in-riosucio-municipality-choco-department-colombia-as-of-17-november-2024
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
  description: "Satellite detected water extent in Riosucio Municipality, Choc\xF3\
    \ Department, Colombia as of 17 November 2024 (Zipped geodatabase)"
  download_url: https://unosat.org/static/unosat_filesystem/4030/FL20241112COL_gdb.zip
  format: Geodatabase
  id: resource_f526b8d2
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20241112COL_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Satellite detected water extent in Riosucio Municipality, Choc\xF3\
    \ Department, Colombia as of 17 November 2024 (Zipped shapefile)"
  download_url: https://unosat.org/static/unosat_filesystem/4030/FL20241112COL_SHP.zip
  format: null
  id: resource_b3e4dfd3
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20241112COL_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-col_unosat_detectedwaterextentriosuc_20241120
spatial:
  bbox: null
  centroid: null
  countries:
  - COL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-11-20'
temporal_resolution: null
title: "Satellite detected water extent in Riosucio Municipality, Choc\xF3 Department,\
  \ Colombia as of 17 November 2024"
version: null
vulnerability: null
---
