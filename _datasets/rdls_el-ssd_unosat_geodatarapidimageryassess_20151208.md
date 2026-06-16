---
attributions:
- entity:
    affiliation: null
    email: null
    name: United Nations Institute for Training and Research - Operational Satellite
      Applications Program (UNITAR-UNOSAT)
    url: https://data.humdata.org/dataset/geodata-of-rapid-satellite-imagery-assessment-and-idp-shelter-analysis-south-december-08-2015
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-rapid-satellite-imagery-assessment-and-idp-shelter-analysis-south-december-08-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-rapid-satellite-imagery-assessment-and-idp-shelter-analysis-south-december-08-2015
dataset_id: rdls_el-ssd_unosat_geodatarapidimageryassess_20151208
description: 'With the rainy season in South Sudan coming to an end in September of
  2015, the United Nations (UN) Country Team and humanitarian actors required information
  to plan efficient delivery of assistance and protection to people in need. Due to
  challenging logistical conditions, it had not been possible to reach this population
  during the rainy season. The United Nations Institute for Training and Research
  ? Operational Satellite Applications Program (UNITAR-UNOSAT) developed a monitoring
  framework for South Sudan, in consultation with United Nations Office for the Coordination
  of Humanitarian Affairs (UNOCHA) and other organizations working in the country.
  To support humanitarian assistance planning, UNITAR-UNOSAT conducted a qualitative
  analysis using high-resolution satellite imagery over portions of the Unity and
  Jonglei states in South Sudan (see Map 1). The analysis identified areas of destruction,
  looting, internally displaced persons (IDPs), and visible cattle, a potentially
  useful indicator of population and wealth distribution in these areas. Subsequently,
  UNITAR-UNOSAT performed a quantitative analysis of possible IDP shelters and estimated
  the number of potentially damaged structures within the same areas. This report
  outlines the methods and results of this analysis.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/geodata-of-rapid-satellite-imagery-assessment-and-idp-shelter-analysis-south-december-08-2015]'
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
    description: IDP shelter structures identified and mapped from satellite imagery
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
    description: Internally displaced persons (IDPs) associated with identified shelter
      locations
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_2
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: CC-BY-4.0
lineage:
  description: UNOSAT analysts conducted rapid satellite imagery assessment by comparing
    multi-temporal satellite images to identify notable changes in settlement patterns
    and IDP shelter locations across South Sudan. Shelter locations and associated
    displaced populations were mapped and vectorized into geospatial datasets to support
    humanitarian planning and assistance delivery during the 2015 post-rainy season
    response.
  sources:
  - id: source_1
    license: null
    name: United Nations Institute for Training and Research - Operational Satellite
      Applications Program (UNITAR-UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/geodata-of-rapid-satellite-imagery-assessment-and-idp-shelter-analysis-south-december-08-2015
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: IDP population displacement assessed through satellite imagery analysis
      during post-flood humanitarian response
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
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
  description: Geodata of Rapid Satellite Imagery Assessment and IDP Shelter Analysis
    - South Sudan (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SS/CE20131218SSD/UNOSAT_RAR_CE20131218SSD_shp.zip
  format: null
  id: resource_8bec1c19
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_RAR_CE20131218SSD_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Rapid Satellite Imagery Assessment and IDP Shelter Analysis
    - South Sudan (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SS/CE20131218SSD/UNOSAT_RAR_CE20131218SSD.gdb.zip
  format: null
  id: resource_c9562a5f
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_RAR_CE20131218SSD.gdb.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-ssd_unosat_geodatarapidimageryassess_20151208
spatial:
  bbox: null
  centroid: null
  countries:
  - SSD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-12-08'
temporal_resolution: null
title: Geodata of Rapid Satellite Imagery Assessment and IDP Shelter Analysis - South
  Sudan
version: null
vulnerability: null
---
