---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/landslides-mudslides-over-kibingo-congonil-kagana-and-ghanga-villages-rutsiro-district-wes
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/landslides-mudslides-over-kibingo-congonil-kagana-and-ghanga-villages-rutsiro-district-wes
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/landslides-mudslides-over-kibingo-congonil-kagana-and-ghanga-villages-rutsiro-district-wes
dataset_id: rdls_hzd-rwa_unosat_detectedlandslidesmudslid_20230509
description: 'UNOSAT code FL20230504RWA, GDACS Id: 1101977 This map illustrates satellite-detected
  landslides / mudslides around Kibingo, Congonil, Kagana and Ghanga Villages in Rutsiro
  District (Western Province, Rwanda) as observed/detected from a Sentinel-2 satellite
  imagery acquired on 07 May 2023 at 08:30 local time. Within the analysed area, about
  2,5 km2 of landslides scars are observed. Some of past landslides seem to have been
  reactivated during these flooding/landslides event. This is a preliminary analysis
  and has not yet been validated in the field. Please send ground feedback to United
  Nations Satellite Centre (UNOSAT).. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/landslides-mudslides-over-kibingo-congonil-kagana-and-ghanga-villages-rutsiro-district-wes]'
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
      intensity_measure: LSI:-
      process: landslide_mudflow
      trigger: null
      type: landslide
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "UNOSAT analysts interpreted Sentinel-2 satellite imagery acquired\
    \ on 7 May 2023 to detect landslide and mudslide scars through visual comparison\
    \ and change detection analysis. Affected areas were digitized and quantified\
    \ (2.5 km\xC2\xB2 total), with notes indicating reactivation of past landslide\
    \ features during the flooding/landslide event. This is a preliminary post-event\
    \ observation requiring field validation."
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
- href: https://data.humdata.org/dataset/landslides-mudslides-over-kibingo-congonil-kagana-and-ghanga-villages-rutsiro-district-wes
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
  description: Satellite detected landslides / mudslides over Kibingo, Congonil, Kagana
    and Ghanga Villages, Rutsiro District, Western Province, Rwanda as of 7 May 2023
    (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3578/FL20230504RWA_gdb.zip
  format: Geodatabase
  id: resource_1ec911fd
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230504RWA_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected landslides / mudslides over Kibingo, Congonil, Kagana
    and Ghanga Villages, Rutsiro District, Western Province, Rwanda as of 7 May 2023
    (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3578/FL20230504RWA_SHP.zip
  format: null
  id: resource_afea8053
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230504RWA_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-rwa_unosat_detectedlandslidesmudslid_20230509
spatial:
  bbox: null
  centroid: null
  countries:
  - RWA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-05-09'
temporal_resolution: null
title: Satellite detected landslides / mudslides over Kibingo, Congonil, Kagana and
  Ghanga Villages, Rutsiro District, Western Province, Rwanda as of 7 May 2023
version: null
vulnerability: null
---
