---
attributions:
- entity:
    affiliation: null
    email: null
    name: iMMAP
    url: https://data.humdata.org/dataset/north-east-nigeria-flood-affected-populations-by-settlement-type-as-of-june-2018
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: IOM Displacement Tracking Matrix (DTM)
    url: https://data.humdata.org/dataset/north-east-nigeria-flood-affected-populations-by-settlement-type-as-of-june-2018
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: CCCM, Shelter and NFI Sector
    url: https://data.humdata.org/dataset/north-east-nigeria-flood-affected-populations-by-settlement-type-as-of-june-2018
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: iMMAP Inc.
  url: https://data.humdata.org/dataset/north-east-nigeria-flood-affected-populations-by-settlement-type-as-of-june-2018
creator:
  affiliation: null
  email: null
  name: iMMAP Inc.
  url: https://data.humdata.org/dataset/north-east-nigeria-flood-affected-populations-by-settlement-type-as-of-june-2018
dataset_id: rdls_el-nga_immap_northeastfloodaffectedpop_20180722
description: 'Flood-affected populations by settlement type as of June 2018. The dataset
  presents the data to LGA level (Admin 2) in all the three crisis-affected states
  of north eastern Nigeria, thus Borno, Yobe and Adamawa. The affected populations
  include households and individuals. The settlement types include Households in IDP
  Camps, Households in Host Communities and provides a computation of affected people
  by settlement type; Camp flood risk mapping as of June 2018. The dataset presents
  the data to LGA level (Admin 2) in IDP camps across all the three crisis-affected
  states of north eastern Nigeria, thus Borno, Yobe and Adamawa; Host Community flood
  risk analysis and mapping as of June 2018. Also includes a CSV file on Flood-affected
  populations by settlement type as of June 2018.. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/north-east-nigeria-flood-affected-populations-by-settlement-type-as-of-june-2018]'
details: null
exposure:
- asset_type:
    description: Flood-affected populations in IDP camps and host communities by settlement
      type at LGA level
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Households in IDP camps and host communities affected by flooding
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
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
  description: Post-event flood impact data compiled from Displacement Tracking Matrix
    (DTM), Flood Risk Vulnerability Assessments, and sector-specific monitoring by
    iMMAP, IOM, CCCM, Shelter and NFI Sector. Affected populations (households and
    individuals) were enumerated by settlement type (IDP camps and host communities)
    and aggregated to LGA (Admin 2) level across Borno, Yobe, and Adamawa states as
    of June 2018.
  sources:
  - id: source_1
    license: null
    name: iMMAP
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: IOM Displacement Tracking Matrix (DTM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: CCCM, Shelter and NFI Sector
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/north-east-nigeria-flood-affected-populations-by-settlement-type-as-of-june-2018
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Flood-affected individuals in IDP camps and host communities across
      three north-eastern Nigerian states
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
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: Flood-affected households in IDP camps and host communities
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_2
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
  description: Flood-affected populations by settlement type as of June 2018. The
    zipped shapefile presents the data to LGA level (Admin 2) in all the three crisis-affected
    states of north eastern Nigeria, thus Borno, Yobe and Adamawa. The affected populations
    includes households and individuals. The settlement types include Households in
    IDP Camps, Households in Host Communities and provides a computation of affected
    people by settlement type.
  download_url: https://data.humdata.org/dataset/ab2cdb0a-0103-408a-93ac-21cf1ce761e3/resource/b9810405-7784-4db2-ac05-92449331c713/download/nga_north_east_nigeria_flood_affected_populations_by_settlement_type_by_lga_june_2018.zip
  format: null
  id: resource_b9810405
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NGA_North_East_Nigeria_Flood_Affected_Populations_by_Settlement_Type_by_LGA_June_2018.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Host Community flood risk analysis and mapping as of June 2018. The
    dataset presents the data to LGA level (Admin 2) in Host Communities across all
    the three crisis-affected states of north eastern Nigeria, thus Borno, Yobe and
    Adamawa.
  download_url: https://data.humdata.org/dataset/ab2cdb0a-0103-408a-93ac-21cf1ce761e3/resource/6792dba6-d9d3-4cb0-8201-b2fbcc77be43/download/nga_north_east_nigeria_host_community_flood_risk_as_of_june_2018.zip
  format: null
  id: resource_6792dba6
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NGA_North_East_Nigeria_Host_Community_Flood_Risk_as_of_June_2018.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-nga_immap_northeastfloodaffectedpop_20180722
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
  start: '2018-07-22'
temporal_resolution: null
title: North East Nigeria Flood-affected Populations by Settlement Type as of June
  2018
version: null
vulnerability: null
---
