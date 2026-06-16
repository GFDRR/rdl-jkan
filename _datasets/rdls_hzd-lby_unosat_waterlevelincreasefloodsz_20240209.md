---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-level-increase-floods-in-zliten-libya-rtf-mnswb-lmyh-fydnt-fy-zlytn-lyby-unosat-live
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-level-increase-floods-in-zliten-libya-rtf-mnswb-lmyh-fydnt-fy-zlytn-lyby-unosat-live
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-level-increase-floods-in-zliten-libya-rtf-mnswb-lmyh-fydnt-fy-zlytn-lyby-unosat-live
dataset_id: rdls_hzd-lby_unosat_waterlevelincreasefloodsz_20240209
description: 'UNOSAT code: FL20240206LBY This application provides geospatial information
  on the ongoing floods in Libya. Important note: The boundaries and names shown,
  and the designations used on this map do not imply official endorsement or acceptance
  by the United Nations. The United Nations Satellite Centre -UNOSAT is not responsible
  for the misuse or misrepresentation of the map.. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/water-level-increase-floods-in-zliten-libya-rtf-mnswb-lmyh-fydnt-fy-zlytn-lyby-unosat-live]'
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
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts reviewed and compared satellite imagery from the flood
    event, identifying water bodies and inundation extent through multi-temporal image
    analysis. Water classification and confidence levels were assigned to delineated
    flood polygons with area calculations in square meters and hectares.
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
- href: https://data.humdata.org/dataset/water-level-increase-floods-in-zliten-libya-rtf-mnswb-lmyh-fydnt-fy-zlytn-lyby-unosat-live
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
  description: "Water level increase / Floods in Zliten (Libya) [\u0627\u0631\u062A\
    \u0641\u0627\u0639 \u0645\u0646\u0633\u0648\u0628 \u0627\u0644\u0645\u064A\u0627\
    \u0647 / \u0641\u064A\u0627\u0636\u0627\u0646\u0627\u062A \u0641\u064A \u0632\u0644\
    \u064A\u062A\u0646 \u060C \u0644\u064A\u0628\u064A\u0627] - UNOSAT Live Web Map\
    \ (Zipped geodatabase)"
  download_url: https://unosat.org/static/unosat_filesystem/3794/FL20240206LBY_gdb.zip
  format: Geodatabase
  id: resource_55f9037b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240206LBY_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Water level increase / Floods in Zliten (Libya) [\u0627\u0631\u062A\
    \u0641\u0627\u0639 \u0645\u0646\u0633\u0648\u0628 \u0627\u0644\u0645\u064A\u0627\
    \u0647 / \u0641\u064A\u0627\u0636\u0627\u0646\u0627\u062A \u0641\u064A \u0632\u0644\
    \u064A\u062A\u0646 \u060C \u0644\u064A\u0628\u064A\u0627] - UNOSAT Live Web Map\
    \ (Zipped shapefile)"
  download_url: https://unosat.org/static/unosat_filesystem/3794/FL20240206LBY_SHP.zip
  format: null
  id: resource_1cb731de
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240206LBY_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-lby_unosat_waterlevelincreasefloodsz_20240209
spatial:
  bbox: null
  centroid: null
  countries:
  - LBY
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-02-09'
temporal_resolution: null
title: "Water level increase / Floods in Zliten (Libya) [\u0627\u0631\u062A\u0641\u0627\
  \u0639 \u0645\u0646\u0633\u0648\u0628 \u0627\u0644\u0645\u064A\u0627\u0647 / \u0641\
  \u064A\u0627\u0636\u0627\u0646\u0627\u062A \u0641\u064A \u0632\u0644\u064A\u062A\
  \u0646 \u060C \u0644\u064A\u0628\u064A\u0627] - UNOSAT Live Web Map"
version: null
vulnerability: null
---
