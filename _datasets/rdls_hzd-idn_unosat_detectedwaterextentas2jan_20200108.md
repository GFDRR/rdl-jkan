---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extent-as-of-2-january-2020-over-banten-dki-jakarta-and-jawa-barat-province-of-indon
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-as-of-2-january-2020-over-banten-dki-jakarta-and-jawa-barat-province-of-indon
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-as-of-2-january-2020-over-banten-dki-jakarta-and-jawa-barat-province-of-indon
dataset_id: rdls_hzd-idn_unosat_detectedwaterextentas2jan_20200108
description: 'UNOSAT code: FL20200101IDN This map illustrates satellite-detected surface
  water in Banten, Dki Jakarta and Jawa Barat Province of Indonesia as observed from
  Sentinel-1 imagery acquired on the 2 January 2020. Approximately 258 km2 of land
  appear to be flooded. This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to UNITAR - UNOSAT. Important Note: Flood
  analysis from Sentinel-1 imagery acquired on 2 January 2020 may seriously underestimate
  presence of standing flood water in built up areas due to backscattering properties
  of the radar signal.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-as-of-2-january-2020-over-banten-dki-jakarta-and-jawa-barat-province-of-indon]'
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
  description: "Sentinel-1 synthetic aperture radar imagery acquired on 2 January\
    \ 2020 was analyzed by UNOSAT through visual interpretation and multi-temporal\
    \ comparison to detect surface water extent changes. Flooded areas were delineated\
    \ and quantified as approximately 258 km\xC2\xB2 across three Indonesian provinces.\
    \ The dataset represents observed post-event hazard extent without field validation."
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
- href: https://data.humdata.org/dataset/water-extent-as-of-2-january-2020-over-banten-dki-jakarta-and-jawa-barat-province-of-indon
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
  description: Satellite detected water extent as of 2 January 2020 over Banten, Dki
    Jakarta and Jawa Barat Province of Indonesia (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/ID/FL20200101IDN/FL20200101IDN_gdb.zip
  format: Geodatabase
  id: resource_83c2dbeb
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20200101IDN_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent as of 2 January 2020 over Banten, Dki
    Jakarta and Jawa Barat Province of Indonesia (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/ID/FL20200101IDN/FL20200101IDN_SHP.zip
  format: null
  id: resource_a714c270
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20200101IDN_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-idn_unosat_detectedwaterextentas2jan_20200108
spatial:
  bbox: null
  centroid: null
  countries:
  - IDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2020-01-08'
temporal_resolution: null
title: Satellite detected water extent as of 2 January 2020 over Banten, Dki Jakarta
  and Jawa Barat Province of Indonesia
version: null
vulnerability: null
---
