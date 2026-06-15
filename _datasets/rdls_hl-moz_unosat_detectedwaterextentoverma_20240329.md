---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/satellite-detected-water-extent-over-maputo-province-mozambique-as-of-27-march-2024
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-over-maputo-province-mozambique-as-of-27-march-2024
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-over-maputo-province-mozambique-as-of-27-march-2024
dataset_id: rdls_hl-moz_unosat_detectedwaterextentoverma_20240329
description: "UNOSAT code: TC20240313MOZ, GDACS ID: 1001053 This map illustrates satellite\
  \ detected surface waters in Maputo province, Mozambique, as observed from a Sentinel-1\
  \ images acquired on 27 March 2024 at 18:23 local time (16:23 UTC). Within the analyzed\
  \ areas of about 2,000 km\xB2, a total of about 45 km\xB2 of lands appear to be\
  \ flooded. This is a preliminary analysis and has not yet been validated in the\
  \ field. Please send ground feedback to the United Nations Satellite Centre (UNOSAT).\
  \ Important note: Flood analysis from radar images may underestimate the presence\
  \ of standing waters in built-up areas and densely vegetated areas due to backscattering\
  \ properties of the radar signal.. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extent-over-maputo-province-mozambique-as-of-27-march-2024]"
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
        process: coastal_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "Sentinel-1 radar imagery acquired on 27 March 2024 was analyzed by\
    \ UNOSAT analysts through visual comparison with reference imagery to detect changes\
    \ in surface water extent. Flooded areas were delineated and quantified within\
    \ a 2,000 km\xB2 study area in Maputo province, resulting in post-event observed\
    \ flood extent data."
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
- href: https://data.humdata.org/dataset/satellite-detected-water-extent-over-maputo-province-mozambique-as-of-27-march-2024
  rel: source
loss:
  losses:
  - asset_category: natural_environment
    asset_dimension: product
    description: "Satellite-detected flooded land area (45 km\xB2) from coastal flood\
      \ event in Maputo province"
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
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
  description: Satellite detected water extent over Maputo province, Mozambique as
    of 27 March 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3813/TC20240313MOZ_gdb.zip
  format: Geodatabase
  id: resource_8d9d0480
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20240313MOZ_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent over Maputo province, Mozambique as
    of 27 March 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3813/TC20240313MOZ_shp.zip
  format: null
  id: resource_b94d7366
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20240313MOZ_shp.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-moz_unosat_detectedwaterextentoverma_20240329
spatial:
  bbox: null
  centroid: null
  countries:
  - MOZ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-03-29'
temporal_resolution: null
title: Satellite detected water extent over Maputo province, Mozambique as of 27 March
  2024
version: null
vulnerability: null
---
