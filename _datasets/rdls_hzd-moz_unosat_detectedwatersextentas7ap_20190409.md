---
attributions:
- entity:
    affiliation: null
    email: null
    name: European Space Agency (ESA) Sentinel-1
    url: https://data.humdata.org/dataset/satellite-detected-waters-extent-as-of-7-april-2019-over-tete-and-zambezia-provinces-mozambique
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-waters-extent-as-of-7-april-2019-over-tete-and-zambezia-provinces-mozambique
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-waters-extent-as-of-7-april-2019-over-tete-and-zambezia-provinces-mozambique
dataset_id: rdls_hzd-moz_unosat_detectedwatersextentas7ap_20190409
description: 'This map illustrates satellite-detected surface waters in Tete and Zambezia
  province, Mozambique as observed from Sentinel-1 imagery acquired on 7 April 2019.
  Within the analysed extent of about 7,800 sq km, a total about 100 sq km of lands
  appear to be flooded as of 7 April 2019. This is a preliminary analysis and has
  not yet been validated in the field. Please send ground feedback to UNITAR - UNOSAT.
  Satellite Data (Post): Sentinel-1 Imagery Date (1): 7 April 2019 Imagery Date (2):
  20 March 2019 Resolution: 10 m Copyright: Copernicus 2019 / ESA Source: ESA. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-waters-extent-as-of-7-april-2019-over-tete-and-zambezia-provinces-mozambique]'
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
  description: Sentinel-1 SAR imagery from 7 April 2019 and 20 March 2019 were compared
    by UNOSAT analysts to identify notable changes in surface water extent. Water
    bodies were delineated through visual interpretation and change detection of radar
    backscatter signatures, resulting in a preliminary map of flooded areas covering
    approximately 100 sq km within the 7,800 sq km study area in Mozambique.
  sources:
  - id: source_1
    license: null
    name: European Space Agency (ESA) Sentinel-1
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-waters-extent-as-of-7-april-2019-over-tete-and-zambezia-provinces-mozambique
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
  description: Satellite detected waters extent, as of 7 April 2019 over Tete and
    Zambezia provinces, Mozambique (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MZ/TC20190312MOZ/TC20190312MOZ_SHP.zip
  format: null
  id: resource_659efece
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20190312MOZ_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected waters extent, as of 7 April 2019 over Tete and
    Zambezia provinces, Mozambique (GeoPackage)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MZ/TC20190312MOZ/TC20190312MOZ.gdb.zip
  format: null
  id: resource_ace96a3f
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20190312MOZ.gdb.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-moz_unosat_detectedwatersextentas7ap_20190409
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
  start: '2019-04-09'
temporal_resolution: null
title: Satellite detected waters extent, as of 7 April 2019 over Tete and Zambezia
  provinces, Mozambique
version: null
vulnerability: null
---
