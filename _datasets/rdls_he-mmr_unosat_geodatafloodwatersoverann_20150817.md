---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-flood-waters-over-ann-and-myebon-area-rakhine-state-myanmar-august-17-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-flood-waters-over-ann-and-myebon-area-rakhine-state-myanmar-august-17-2015
dataset_id: rdls_he-mmr_unosat_geodatafloodwatersoverann_20150817
description: 'This map illustrates satellite-detected flood waters over western Rakhine
  State, Myanmar, in the areas of Ann and Myebon townships, as imaged by the ALOS-2
  / PALSAR-2 satellite on 16 August 2015. In the analyzed area a total of ~24,600
  ha of lands are affected by floods, mainly agricultural and/or paddy fields. The
  surface covered with water in the analyzed area has increased from a pre-flood level
  of 10.2% to 15.2% during the flood period. It is likely that flood waters have been
  systematically underestimated along highly vegetated areas near the main river banks,
  and within built-up urban areas because of the special characteristics of the satellite
  data used. This is a preliminary analysis and has not yet been validated in the
  field. Please send ground feedback to UNITAR-UNOSAT.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/geodata-of-flood-waters-over-ann-and-myebon-area-rakhine-state-myanmar-august-17-2015]'
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
    description: Agricultural and paddy field areas affected by flood waters
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
license: CC-BY-4.0
lineage:
  description: UNOSAT analysts compared pre-flood and post-flood ALOS-2/PALSAR-2 satellite
    imagery acquired on 16 August 2015 to detect and delineate flood water extent
    over Ann and Myebon townships. Water surface area was quantified from the satellite-derived
    classification, with confidence assessments and field validation notes recorded
    for quality assurance.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/geodata-of-flood-waters-over-ann-and-myebon-area-rakhine-state-myanmar-august-17-2015
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
  description: Geodata of Flood Waters Over Ann and Myebon area, Rakhine State, Myanmar
    (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MM/FL20150703MMR/FL20150703MMR_shp.zip
  format: null
  id: resource_b7cf14e4
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20150703MMR_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Flood Waters Over Ann and Myebon area, Rakhine State, Myanmar
    (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MM/FL20150703MMR/FL20150703MMR.gdb.zip
  format: null
  id: resource_c5353a65
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20150703MMR.gdb.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-mmr_unosat_geodatafloodwatersoverann_20150817
spatial:
  bbox: null
  centroid: null
  countries:
  - MMR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-08-17'
temporal_resolution: null
title: Geodata of Flood Waters Over Ann and Myebon area, Rakhine State, Myanmar
version: null
vulnerability: null
---
