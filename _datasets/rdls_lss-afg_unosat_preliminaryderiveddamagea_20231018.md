---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/preliminary-satellite-derived-damage-assessment-6-3m-earthquake-of-15-october-2023-03-36-u
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/preliminary-satellite-derived-damage-assessment-6-3m-earthquake-of-15-october-2023-03-36-u
dataset_id: rdls_lss-afg_unosat_preliminaryderiveddamagea_20231018
description: 'UNOSAT code EQ20231008AFG, GDACS Id: 1394952 Status: Destroyed structures
  observed Further action(s): full assessment to be conducted Widespread destroyed
  structures observed in several villages North and Northwest of Herat in Zindajan
  & Hinjil Districts, Hirat Province folowing the 15 October 2023 M6.3 earthquake;
  Temporary shelters observed in the affected villages as of 15 October 2023; Additional
  damage to structures are observed from an image acquired on15 October 2023; The
  15th of October 2023 earthquake has triggered additional damage in areas already
  damaged by the 9th and 11th October 2023 earthquakes.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/preliminary-satellite-derived-damage-assessment-6-3m-earthquake-of-15-october-2023-03-36-u]'
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
hazard: null
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts reviewed and compared satellite imagery acquired before
    and after the 15 October 2023 M6.3 earthquake in Herat Province, Afghanistan,
    identifying destroyed structures and damage patterns through visual interpretation
    of multi-temporal satellite data. Damage polygons were delineated and attributed
    with site identifiers and area measurements to produce a post-event damage assessment
    geodatabase.
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
- href: https://data.humdata.org/dataset/preliminary-satellite-derived-damage-assessment-6-3m-earthquake-of-15-october-2023-03-36-u
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from M6.3 earthquake of 15 October
      2023 in Zindajan & Hinjil Districts
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_1
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
  description: Preliminary satellite-derived damage assessment - 6.3M earthquake of
    15 October 2023 03:36 UTC - Zindajan & Hinjil Districts, Hirat Province, Afghanistan
    (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3692/EQ20231008AFG_gdb.zip
  format: Geodatabase
  id: resource_66615453
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20231008AFG_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Preliminary satellite-derived damage assessment - 6.3M earthquake of
    15 October 2023 03:36 UTC - Zindajan & Hinjil Districts, Hirat Province, Afghanistan
    (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3692/EQ20231008AFG_SHP.zip
  format: null
  id: resource_49671676
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20231008AFG_SHP.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-afg_unosat_preliminaryderiveddamagea_20231018
spatial:
  bbox: null
  centroid: null
  countries:
  - AFG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-10-18'
temporal_resolution: null
title: Preliminary satellite-derived damage assessment - 6.3M earthquake of 15 October
  2023 03:36 UTC - Zindajan & Hinjil Districts, Hirat Province, Afghanistan
version: null
vulnerability: null
---
