---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extent-over-sambava-and-vohemar-districts-sava-region-madagascar-as-of-01-april-2024
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-sambava-and-vohemar-districts-sava-region-madagascar-as-of-01-april-2024
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-sambava-and-vohemar-districts-sava-region-madagascar-as-of-01-april-2024
dataset_id: rdls_hzd-mdg_unosat_detectedwaterextentoversa_20240404
description: "UNOSAT code: TC20240328MDG, GDACS ID: 1001057 This map illustrates satellite-detected\
  \ water extent in Sambava and Vohemar Districts, Sava Region, Madagascar as observed\
  \ from a TanDEM-X satellite image acquired on 01 April 2024 at 18:09 local time\
  \ (15:09 UTC). Within the analysed area of about 850 km\xB2, a total of about 10\
  \ km\xB2 of lands appear to be affected with flood waters. This is a preliminary\
  \ analysis and has not yet been validated in the field. Please send ground feedback\
  \ to the United Nations Satellite Centre (UNOSAT). Important note: Flood analysis\
  \ from radar images may underestimate the presence of standing waters in built-up\
  \ areas and densely vegetated areas due to backscattering properties of the radar\
  \ signal.. [Source: This metadata record was automatically extracted from the Humanitarian\
  \ Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-over-sambava-and-vohemar-districts-sava-region-madagascar-as-of-01-april-2024]"
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
  event_sets:
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
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: "TanDEM-X satellite radar imagery acquired on 01 April 2024 was analyzed\
    \ by UNOSAT analysts through visual interpretation and multi-temporal comparison\
    \ to detect changes in water extent. Flood-affected areas were delineated and\
    \ quantified (approximately 10 km\xB2 of inundation within 850 km\xB2 study area)\
    \ and delivered as vector geodatabase and shapefile products with confidence and\
    \ validation metadata."
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
- href: https://data.humdata.org/dataset/water-extent-over-sambava-and-vohemar-districts-sava-region-madagascar-as-of-01-april-2024
  rel: source
loss: null
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
  description: Satellite detected water extent over Sambava and Vohemar Districts,
    Sava Region, Madagascar as of 01 April 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3817/TC20240328MDG_gdb.zip
  format: Geodatabase
  id: resource_4acbe58c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20240328MDG_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent over Sambava and Vohemar Districts,
    Sava Region, Madagascar as of 01 April 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3817/TC20240328MDG_SHP.zip
  format: null
  id: resource_a8b7ae1a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20240328MDG_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-mdg_unosat_detectedwaterextentoversa_20240404
spatial:
  bbox: null
  centroid: null
  countries:
  - MDG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-04-04'
temporal_resolution: null
title: Satellite detected water extent over Sambava and Vohemar Districts, Sava Region,
  Madagascar as of 01 April 2024
version: null
vulnerability: null
---
