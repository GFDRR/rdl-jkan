---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extent-in-ag-geneina-and-kereneik-west-darfur-state-sudan-as-of-5-september-2024s-of
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-ag-geneina-and-kereneik-west-darfur-state-sudan-as-of-5-september-2024s-of
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-ag-geneina-and-kereneik-west-darfur-state-sudan-as-of-5-september-2024s-of
dataset_id: rdls_hzd-sdn_unosat_detectedwaterextentaggene_20240906
description: "UNOSAT code: FL20240826SDN, GDACS ID: 1102854 This map illustrates satellite-detected\
  \ water extents in the two towns of Ag Geneina and Kereneik, West Darfur State,\
  \ Sudan as observed from a Sentinel-2 image acquired on 5 September 2024 at 11:06\
  \ local time (09:06 UTC). Within the analysed area of about 700 km\xB2, a total\
  \ of about 50 km\xB2 of land appears to be affected by floodwaters. This is a preliminary\
  \ analysis and has not yet been validated in the field. Please send ground feedback\
  \ to the United Nations Satellite Centre (UNOSAT).. [Source: This metadata record\
  \ was automatically extracted from the Humanitarian Data Exchange (HDX); Original\
  \ dataset: https://data.humdata.org/dataset/water-extent-in-ag-geneina-and-kereneik-west-darfur-state-sudan-as-of-5-september-2024s-of]"
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
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: "Sentinel-2 satellite imagery acquired on 5 September 2024 was analyzed\
    \ by UNOSAT analysts through visual interpretation and comparison with reference\
    \ imagery to detect and delineate water extents. The resulting water extent polygons\
    \ (approximately 50 km\xB2 across 700 km\xB2 study area) were extracted and provided\
    \ in geodatabase and shapefile formats as preliminary, field-unvalidated observations."
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
- href: https://data.humdata.org/dataset/water-extent-in-ag-geneina-and-kereneik-west-darfur-state-sudan-as-of-5-september-2024s-of
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
  description: Satellite detected water extent in Ag Geneina and Kereneik, West Darfur
    State, Sudan as of 5 September 2024s of 5 September 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3953/FL20240826SDN_gdb.zip
  format: Geodatabase
  id: resource_f26363ac
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
  description: Satellite detected water extent in Ag Geneina and Kereneik, West Darfur
    State, Sudan as of 5 September 2024s of 5 September 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3953/FL20240826SDN_SHP.zip
  format: null
  id: resource_1a0635d2
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240826SDN_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-sdn_unosat_detectedwaterextentaggene_20240906
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
  start: '2024-09-06'
temporal_resolution: null
title: Satellite detected water extent in Ag Geneina and Kereneik, West Darfur State,
  Sudan as of 5 September 2024s of 5 September 2024
version: null
vulnerability: null
---
