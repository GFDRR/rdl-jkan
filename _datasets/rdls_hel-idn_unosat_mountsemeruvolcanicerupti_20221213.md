---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/mount-semeru-volcanic-eruption-jawa-timur-province-indonesia-unosat-live-web-map
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/mount-semeru-volcanic-eruption-jawa-timur-province-indonesia-unosat-live-web-map
dataset_id: rdls_hel-idn_unosat_mountsemeruvolcanicerupti_20221213
description: 'UNOSAT code VO20221206IDN, GDACS Id: 1000057 Live web map providing
  geospatial information potentially affected areas by pyroclastic flow/deposits after
  the December 2022 Mount Semeru volcanic eruption in East Java. This web map gives
  an updated overview over potentially affected structures and affected structures
  based on very high-resolution satellite images and also Pyroclastic flow/deposits..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/mount-semeru-volcanic-eruption-jawa-timur-province-indonesia-unosat-live-web-map]'
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
    description: Building structures in areas potentially affected by pyroclastic
      flow deposits
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
  event_sets:
  - analysis_type: probabilistic
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: h_vaf:mm
      process: pyroclastic_flow
      trigger: null
      type: volcanic
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts reviewed and compared very high-resolution satellite
    imagery acquired after the December 2022 Mount Semeru eruption to delineate pyroclastic
    flow and deposit extents, then overlaid building footprints to identify potentially
    and confirmed affected structures in East Java Province, Indonesia.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/mount-semeru-volcanic-eruption-jawa-timur-province-indonesia-unosat-live-web-map
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from pyroclastic flow and volcanic deposits
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_volcanic
      intensity_measure: h_vaf:mm
      process: null
      trigger: null
      type: volcanic
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
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
  description: Mount Semeru volcanic eruption, Jawa Timur Province, Indonesia - UNOSAT
    Live Web Map (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3463/VO20221206IDN_gdb.zip
  format: Geodatabase
  id: resource_5fa5c1ae
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VO20221206IDN_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Mount Semeru volcanic eruption, Jawa Timur Province, Indonesia - UNOSAT
    Live Web Map (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3463/VO202212006IDN_SHP.zip
  format: null
  id: resource_ff0a0ad6
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VO202212006IDN_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-idn_unosat_mountsemeruvolcanicerupti_20221213
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
  start: '2022-12-13'
temporal_resolution: null
title: Mount Semeru volcanic eruption, Jawa Timur Province, Indonesia - UNOSAT Live
  Web Map
version: null
vulnerability: null
---
