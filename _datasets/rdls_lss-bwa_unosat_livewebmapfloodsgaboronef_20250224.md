---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/unosat-live-web-map-floods-in-gaborone-botswana-february-2025
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-live-web-map-floods-in-gaborone-botswana-february-2025
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-live-web-map-floods-in-gaborone-botswana-february-2025
dataset_id: rdls_lss-bwa_unosat_livewebmapfloodsgaboronef_20250224
description: 'UNOSAT code: FL20250220BWA, GDACS ID: 1103128 This application provides
  flood impact assessments for Floods in Gaborone, Botswana Important note: The boundaries
  and names shown, and the designations used on this map do not imply official endorsement
  or acceptance by the United Nations. The designations employed and the presentation
  of material on this map do not imply the expression of any opinion whatsoever on
  the part of the Secretariat of the United Nations concerning the legal status of
  any country, territory, city or area or of its authorities, or concerning the delimitation
  of its frontiers or boundaries.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/unosat-live-web-map-floods-in-gaborone-botswana-february-2025]'
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts reviewed and compared satellite imagery from the February
    2025 flood event in Gaborone, identifying notable changes and damage patterns.
    Damage assessments were conducted through visual interpretation of satellite data,
    with confidence levels and field validation flags recorded for each affected settlement
    and structure.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/unosat-live-web-map-floods-in-gaborone-botswana-february-2025
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from February 2025 floods in Gaborone
      derived from satellite imagery analysis
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
  description: UNOSAT Live web map -Floods in Gaborone, Botswana, February 2025 (Zipped
    geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4079/FL20250220BWA_gdb.zip
  format: Geodatabase
  id: resource_8ae8b972
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20250220BWA_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: UNOSAT Live web map -Floods in Gaborone, Botswana, February 2025 (Zipped
    shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4079/FL20250220BWA_SHP.zip
  format: null
  id: resource_b6103188
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20250220BWA_SHP.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-bwa_unosat_livewebmapfloodsgaboronef_20250224
spatial:
  bbox: null
  centroid: null
  countries:
  - BWA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-02-24'
temporal_resolution: null
title: UNOSAT Live web map -Floods in Gaborone, Botswana, February 2025
version: null
vulnerability: null
---
