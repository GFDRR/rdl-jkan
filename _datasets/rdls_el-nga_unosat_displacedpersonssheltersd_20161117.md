---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/displaced-persons-shelters-in-dalakaleri-nigeria
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/displaced-persons-shelters-in-dalakaleri-nigeria
dataset_id: rdls_el-nga_unosat_displacedpersonssheltersd_20161117
description: 'This map illustrates satellite-detected displaced persons shelters in
  the Muna settlement near Dalakaleri, Nigeria, 6 km east of Maidugur''s city on the
  main road that connect Maidugur to Dikwa. UNITAR-UNOSAT analysis of satellite imagery
  acquired 5 September 2016 revealed a total of 2,597 shelters and 22 infrastructure
  and support buildings within the Muna compound. In addition there are 203 detected
  shelters outside the settlement, grouped across the road. Finally, as of 5 September
  2016 there are 120 newly constructed shelters arranged in five rows in the norther
  part of the Muna compound. This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to UNITAR - UNOSAT.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/displaced-persons-shelters-in-dalakaleri-nigeria]'
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
    description: Displaced persons shelters detected via satellite imagery, including
      temporary structures and support buildings in the Muna settlement
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts reviewed satellite imagery acquired on 5 September
    2016 and compared multi-temporal images to detect and map displaced persons shelters
    and support infrastructure in the Muna settlement. Shelter counts and spatial
    locations were extracted through manual interpretation of satellite imagery with
    confidence assessments and field validation flags recorded for each detected structure.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/displaced-persons-shelters-in-dalakaleri-nigeria
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Displaced persons shelters affected by complex emergency/conflict
      in Dalakaleri, Nigeria
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
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
  description: Displaced Persons Shelters in Dalakaleri, Nigeria (Zipped geodatabase)
  download_url: https://cern.ch/unosat-maps/NG/CE20140617NGA/CE20140617NGA_Muna_20160905.gdb.zip
  format: Geodatabase
  id: resource_cfeeb0f9
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20140617NGA_Muna_20160905.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Displaced Persons Shelters in Dalakaleri, Nigeria (Zipped shapefile)
  download_url: https://cern.ch/unosat-maps/NG/CE20140617NGA/CE20140617NGA_Muna_20160905_shp.zip
  format: null
  id: resource_ef2b6d9d
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20140617NGA_Muna_20160905_shp.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-nga_unosat_displacedpersonssheltersd_20161117
spatial:
  bbox: null
  centroid: null
  countries:
  - NGA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-11-17'
temporal_resolution: null
title: Displaced Persons Shelters in Dalakaleri, Nigeria
version: null
vulnerability: null
---
