---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/satellite-flood-water-extent-between-the-nova-kakhovka-dam-wall-and-the-dnipro-river-mouth
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-flood-water-extent-between-the-nova-kakhovka-dam-wall-and-the-dnipro-river-mouth
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-flood-water-extent-between-the-nova-kakhovka-dam-wall-and-the-dnipro-river-mouth
dataset_id: rdls_hzd-ukr_unosat_floodwaterextentbetweenno_20230622
description: "UNOSAT code FL20230606UKR This map illustrates satellite-detected flood\
  \ waters along the 90km downstream of Dnipro River between the damaged Nova Kakhovka\
  \ Dam wall and the Dnipro River mouth in Ukraine as observed from a Sentinel-1 images\
  \ acquired on 21 June 2023 at 15:36 UTC. Within the analysed area of about 10,800\
  \ km\xB2, about 20 km\xB2 of land appear to remain flooded. This is a preliminary\
  \ analysis and has not yet been validated in the field. Please send ground feedback\
  \ to United Nations Satellite Centre (UNOSAT).. [Source: This metadata record was\
  \ automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:\
  \ https://data.humdata.org/dataset/satellite-flood-water-extent-between-the-nova-kakhovka-dam-wall-and-the-dnipro-river-mouth]"
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
  description: Sentinel-1 satellite imagery acquired on 21 June 2023 was analyzed
    by UNOSAT analysts through visual interpretation and multi-temporal comparison
    to detect and delineate flood water extent along the Dnipro River downstream of
    the damaged Nova Kakhovka Dam. The resulting flood extent polygons with area measurements
    represent observed post-event hazard conditions in a preliminary, field-unvalidated
    assessment.
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
- href: https://data.humdata.org/dataset/satellite-flood-water-extent-between-the-nova-kakhovka-dam-wall-and-the-dnipro-river-mouth
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
  description: Satellite Flood water Extent between the Nova Kakhovka Dam Wall and
    the Dnipro River mouth, Khersonska Oblast, Ukraine as of 21 June 2023 (Zipped
    shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3631/FL20230606UKR_SHP.zip
  format: null
  id: resource_b58e5ce4
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230606UKR_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite Flood water Extent between the Nova Kakhovka Dam Wall and
    the Dnipro River mouth, Khersonska Oblast, Ukraine as of 21 June 2023 (Zipped
    geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3631/FL20230606UKR.gdb.zip
  format: Geodatabase
  id: resource_5d4f7f9f
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230606UKR.gdb.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-ukr_unosat_floodwaterextentbetweenno_20230622
spatial:
  bbox: null
  centroid: null
  countries:
  - UKR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-06-22'
temporal_resolution: null
title: Satellite Flood water Extent between the Nova Kakhovka Dam Wall and the Dnipro
  River mouth, Khersonska Oblast, Ukraine as of 21 June 2023
version: null
vulnerability: null
---
