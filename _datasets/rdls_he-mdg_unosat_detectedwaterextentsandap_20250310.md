---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extents-in-andapa-district-sava-region-madagascar-as-of-9-march-2025
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-in-andapa-district-sava-region-madagascar-as-of-9-march-2025
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-in-andapa-district-sava-region-madagascar-as-of-9-march-2025
dataset_id: rdls_he-mdg_unosat_detectedwaterextentsandap_20250310
description: "UNOSAT code: TC20250308MDG, GDACS ID: 1154 This map illustrates the\
  \ potentially affected cropland in Andapa District, Sava Region, Madagascar, based\
  \ on RCM-2 satellite images acquired on 9 March 2025. In the analyzed area of approximately\
  \ 680 km\xB2, about 145 km\xB2 of cropland is identified, of which about 20 km\xB2\
  \ appears to be affected by floodwaters. This is a preliminary analysis and has\
  \ not yet been validated on the ground. Ground feedback is requested and can be\
  \ sent to the United Nations Satellite Centre (UNOSAT). Important Note: Flood analysis\
  \ based on radar images may underestimate the presence of standing water in built-up\
  \ or densely vegetated areas due to the backscattering properties of the radar signal.\
  \ as of 9 March 2025. [Source: This metadata record was automatically extracted\
  \ from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extents-in-andapa-district-sava-region-madagascar-as-of-9-march-2025]"
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure:
- asset_type:
    description: Cropland inventory in Andapa District classified by flood exposure
      status
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_1
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
hazard:
  event_sets:
  - analysis_type: probabilistic
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
  description: "RCM-2 satellite radar images acquired on 9 March 2025 were analyzed\
    \ by UNOSAT analysts using change detection methodology comparing pre- and post-event\
    \ imagery to delineate water extents and quantify flood-affected cropland area\
    \ (20 km\xB2 of 145 km\xB2 total cropland) in Andapa District. The analysis is\
    \ preliminary and unvalidated on the ground."
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
- href: https://data.humdata.org/dataset/water-extents-in-andapa-district-sava-region-madagascar-as-of-9-march-2025
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
  description: Satellite detected water extents in Andapa District, Sava Region, Madagascar
    as of 9 March 2025 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4086/TC20250308MDG_gdb.zip
  format: Geodatabase
  id: resource_a51e2448
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20250308MDG_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents in Andapa District, Sava Region, Madagascar
    as of 9 March 2025 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4086/TC20250308MDG_SHP.zip
  format: null
  id: resource_a5b16dfc
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20250308MDG_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-mdg_unosat_detectedwaterextentsandap_20250310
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
  start: '2025-03-10'
temporal_resolution: null
title: Satellite detected water extents in Andapa District, Sava Region, Madagascar
  as of 9 March 2025
version: null
vulnerability: null
---
