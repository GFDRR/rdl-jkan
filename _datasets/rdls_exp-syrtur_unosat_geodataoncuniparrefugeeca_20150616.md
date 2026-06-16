---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-oncunipar-refugee-camp-merkez-district-kilis-province-turkey-june-16-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-oncunipar-refugee-camp-merkez-district-kilis-province-turkey-june-16-2015
dataset_id: rdls_exp-syrtur_unosat_geodataoncuniparrefugeeca_20150616
description: 'This map illustrates satellite-detected shelters in the Oncunipar Refugee
  Camp in Merkez District, Kilis Province, Turkey. As of 05 June 2015, UNOSAT analyzed
  a total of 2,469 shelters as well as 67 infrastructure and support buildings within
  the 40.7 ha of the camp. A new 10 ha area has been built since December 2014 containing
  506 of the 2,469 shelter structures. This is a preliminary analysis and has not
  yet been validated in the field. Please send ground feedback to UNITAR - UNOSAT..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-oncunipar-refugee-camp-merkez-district-kilis-province-turkey-june-16-2015]'
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
    description: Satellite-detected shelter structures in refugee camp, classified
      by type (formal tents and support buildings)
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
- asset_type:
    description: Infrastructure and support buildings within the refugee camp
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: CC-BY-4.0
lineage:
  description: UNOSAT analysts reviewed and compared satellite imagery from multiple
    dates to detect shelter structures and infrastructure within the Oncunipar refugee
    camp. Shelter counts and spatial footprints were extracted through manual interpretation
    of satellite imagery, with confidence levels assigned to each detected structure.
    The dataset represents a snapshot as of June 2015 and includes newly constructed
    areas since December 2014.
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
- href: https://data.humdata.org/dataset/geodata-of-oncunipar-refugee-camp-merkez-district-kilis-province-turkey-june-16-2015
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
  description: Geodata of Oncunipar Refugee Camp, Merkez District, Kilis Province,
    Turkey (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SY/CE20130604SYR/CE20130604SYR_Oncunipar_shp.zip
  format: null
  id: resource_234203ca
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20130604SYR_Oncunipar_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Oncunipar Refugee Camp, Merkez District, Kilis Province,
    Turkey (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SY/CE20130604SYR/CE20130604SYR_Oncunipar.gdb.zip
  format: null
  id: resource_2d6dc163
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20130604SYR_Oncunipar.gdb.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-syrtur_unosat_geodataoncuniparrefugeeca_20150616
spatial:
  bbox: null
  centroid: null
  countries:
  - SYR
  - TUR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-06-16'
temporal_resolution: null
title: Geodata of Oncunipar Refugee Camp, Merkez District, Kilis Province, Turkey
version: null
vulnerability: null
---
