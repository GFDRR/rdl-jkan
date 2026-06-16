---
attributions:
- entity:
    affiliation: null
    email: null
    name: Nepal National Geospatial Agency IWG-R3
    url: https://data.humdata.org/dataset/nepal-covered-and-impassable-road-as-of-28-apr-2015
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX
  url: https://data.humdata.org/dataset/nepal-covered-and-impassable-road-as-of-28-apr-2015
creator:
  affiliation: null
  email: null
  name: Nepal National Geospatial Agency IWG-R3
  url: https://data.humdata.org/dataset/nepal-covered-and-impassable-road-as-of-28-apr-2015
dataset_id: rdls_el-npl_hdx_coveredimpassableroadsas2_20150428
description: 'Geodata of Nepal earthquake covered and impassable road shared publicly
  by NGA''s Open Data Application. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/nepal-covered-and-impassable-road-as-of-28-apr-2015]'
details: null
exposure:
- asset_type:
    description: Road network geometry classified by passability status post-earthquake
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: length
      unit: null
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Road network data was assessed and classified by the Nepal National
    Geospatial Agency in the immediate aftermath of the April 2015 earthquake, with
    segments categorized as either covered (blocked by debris/landslides) or impassable
    (damaged/destroyed). The resulting geodata represents direct earthquake impacts
    on transportation infrastructure.
  sources:
  - id: source_1
    license: null
    name: Nepal National Geospatial Agency IWG-R3
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/nepal-covered-and-impassable-road-as-of-28-apr-2015
  rel: source
loss:
  losses:
  - asset_category: infrastructure
    asset_dimension: structure
    description: Direct damage to road infrastructure from the 2015 Nepal earthquake,
      recorded as covered or impassable road segments
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
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
  description: 'Nepal: Covered and impassable roads as of 28 Apr 2015 (Polyline of
    covered roads in Nepal as of 27 Apr 2015 in zipped shapefiles (5 kb))'
  download_url: https://data.humdata.org/dataset/52cbd5f7-ffc2-456a-8323-19f841e0f243/resource/0072d723-a545-4643-9bbc-d2c994586d39/download/covered-roads-nepal-april-27th-2015-2.zip
  format: null
  id: resource_0072d723
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Covered_Roads_Nepal_April_27th_2015.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Polyline of impassable roads in Nepal as of 28 Apr 2015, in zipped
    shapefiles (3 kb)
  download_url: https://data.humdata.org/dataset/52cbd5f7-ffc2-456a-8323-19f841e0f243/resource/1953e6e8-9d52-4d65-899d-d7c31ce20357/download/impassable-roads-nepal-april-28th-2015.zip
  format: null
  id: resource_1953e6e8
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Impassable_Roads_Nepal_April_28th_2015.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-npl_hdx_coveredimpassableroadsas2_20150428
spatial:
  bbox: null
  centroid: null
  countries:
  - NPL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-04-28'
temporal_resolution: null
title: 'Nepal: Covered and impassable roads as of 28 Apr 2015'
version: null
vulnerability: null
---
