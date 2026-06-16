---
attributions:
- entity:
    affiliation: null
    email: null
    name: FEWS Net
    url: https://data.humdata.org/dataset/somalia-food-insecurity-phase-east-africa-drought-2011-fewsnet-07-22-2011
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Regional Centre for Mapping of Development Resources (RCMRD) (inactive)
  url: https://data.humdata.org/dataset/somalia-food-insecurity-phase-east-africa-drought-2011-fewsnet-07-22-2011
creator:
  affiliation: null
  email: null
  name: Regional Centre for Mapping of Development Resources (RCMRD) (inactive)
  url: https://data.humdata.org/dataset/somalia-food-insecurity-phase-east-africa-drought-2011-fewsnet-07-22-2011
dataset_id: rdls_lss-som_rcmrd_foodinsecurityphaseeastaf_20110722
description: 'Food security classification at administrative level 1 in Somalia in
  relation to drought in the Horn of Africa. Source: FEWS Net. Date: 07/22/2011..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/somalia-food-insecurity-phase-east-africa-drought-2011-fewsnet-07-22-2011]'
details: This dataset has been made available on HDX by a direct link to Regional
  Centre for mapping of Resources for development portal
exposure: []
hazard: null
license: CC0-1.0
lineage:
  description: FEWS Net conducted sample surveys and integrated drought hazard information
    with population vulnerability data to classify food insecurity phases at administrative
    level 1 in Somalia during the 2011 East Africa drought crisis.
  sources:
  - id: source_1
    license: null
    name: FEWS Net
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/somalia-food-insecurity-phase-east-africa-drought-2011-fewsnet-07-22-2011
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Food insecurity classification of population affected by East Africa
      drought
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
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
purpose: Sample Survey
referenced_by: []
resources:
- access_url: http://horn.rcmrd.org/geoserver/wfs?format_options=charset%3AUTF-8&typename=geonode%3Asom_food_security_apr_sep11&outputFormat=SHAPE-ZIP&version=1.0.0&service=WFS&request=GetFeature
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: 'Food security classification at administrative level 1 in Somalia
    in relation to drought in the Horn of Africa. Source: FEWS Net. Date: 07/22/2011.'
  download_url: null
  format: null
  id: resource_c6e5f4ca
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Food security classification at administrative level 1 in Somalia
- access_url: http://horn.rcmrd.org/geoserver/wfs?typename=geonode%3Aeri_affected_regions&outputFormat=json&version=1.0.0&request=GetFeature&service=WFS
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: 'Food security classification at administrative level 1 in Somalia
    in relation to drought in the Horn of Africa. Source: FEWS Net. Date: 07/22/2011.'
  download_url: null
  format: null
  id: resource_968f9103
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Food security classification at administrative level 1 in Somalia in relation
    to drought in the Horn of Africa
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-som_rcmrd_foodinsecurityphaseeastaf_20110722
spatial:
  bbox: null
  centroid: null
  countries:
  - SOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2011-07-22'
temporal_resolution: null
title: Somalia Food Insecurity Phase (East Africa Drought 2011) FEWSNET
version: null
vulnerability: null
---
