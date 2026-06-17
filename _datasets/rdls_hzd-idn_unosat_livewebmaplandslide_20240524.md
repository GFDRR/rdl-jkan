---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/unosat-live-web-map-landslide-in-indonesia
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-live-web-map-landslide-in-indonesia
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-live-web-map-landslide-in-indonesia
dataset_id: rdls_hzd-idn_unosat_livewebmaplandslide_20240524
description: 'UNOSAT code: LS20240512IDN, GDACS ID: 1102617 This application provides
  geospatial information on the ongoing landslide in Indonesia Important note: The
  boundaries and names shown, and the designations used on this map do not imply official
  endorsement or acceptance by the United Nations. The United Nations Satellite Centre.
  UNOSAT is not responsible for the misuse or misrepresentation of the map.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/unosat-live-web-map-landslide-in-indonesia]'
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
      process: landslide_general
      trigger: null
      type: landslide
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: landslide
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts reviewed and compared satellite imagery to identify
    and delineate the spatial extent of the landslide event. The resulting geodatabase
    and shapefile contain mapped landslide polygons with area measurements and metadata
    (sensor date, sensor ID, event code) derived from post-event satellite observation.
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
- href: https://data.humdata.org/dataset/unosat-live-web-map-landslide-in-indonesia
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
  description: UNOSAT Live Web map - Landslide in Indonesia (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3853/LS20240512IDN_gdb.zip
  format: Geodatabase
  id: resource_7baad8ee
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LS20240512IDN_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: UNOSAT Live Web map - Landslide in Indonesia (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3853/LS20240512IDN_SHP.zip
  format: null
  id: resource_287d10a0
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LS20240512IDN_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-idn_unosat_livewebmaplandslide_20240524
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
  start: '2024-05-24'
temporal_resolution: null
title: UNOSAT Live Web map - Landslide in Indonesia
version: null
vulnerability: null
---
