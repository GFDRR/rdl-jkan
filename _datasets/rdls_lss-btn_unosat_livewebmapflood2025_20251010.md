---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-live-web-map-flood-in-bhutan-2025
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-live-web-map-flood-in-bhutan-2025
dataset_id: rdls_lss-btn_unosat_livewebmapflood2025_20251010
description: 'UNOSAT code: FL20251006BTN This application provides flood impact assessments
  in Bhutan Important note: The boundaries and names shown, and the designations used
  on this map do not imply official endorsement or acceptance by the United Nations.
  The United Nations Satellite Centre - UNOSAT is not responsible for the misuse or
  misrepresentation of the map. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/unosat-live-web-map-flood-in-bhutan-2025]'
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
  description: UNOSAT analysts reviewed and compared multi-temporal satellite imagery
    to detect notable changes and assess flood damage to settlements in Bhutan. Damage
    classifications were recorded with confidence levels and field validation flags,
    producing a georeferenced damage assessment dataset with settlement-level impact
    records.
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
- href: https://data.humdata.org/dataset/unosat-live-web-map-flood-in-bhutan-2025
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from flood event in Bhutan derived
      from satellite imagery analysis
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
  description: UNOSAT Live Web Map-Flood in Bhutan 2025 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4208/FL20251006BTN_gdb.zip
  format: Geodatabase
  id: resource_ab02d808
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20251006BTN_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: UNOSAT Live Web Map-Flood in Bhutan 2025 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4208/FL20251006BTN_SHP.zip
  format: null
  id: resource_d7f15ffe
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20251006BTN_SHP.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-btn_unosat_livewebmapflood2025_20251010
spatial:
  bbox: null
  centroid: null
  countries:
  - BTN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-10-10'
temporal_resolution: null
title: UNOSAT Live Web Map-Flood in Bhutan 2025
version: null
vulnerability: null
---
