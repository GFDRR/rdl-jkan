---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Patrick Kabatha
  url: https://geoportal.rcmrd.org/catalogue/#/dataset/58
creator:
  affiliation: null
  email: null
  name: Patrick Kabatha
  url: https://geoportal.rcmrd.org/catalogue/#/dataset/58
dataset_id: rdls_exp-rwa_rcmrd_landcover2010schemei
description: 'Land Cover maps were developed for Green Houses gases Inventories to
  provide baseline data for Land use, land-use change and forestry (LULUCF)sector.
  The coverage for the Land Cover maps is NINE Eastern and Southern Africa (ESA) countries
  namely: Ethiopia, Botswana, Lesotho, Malawi, Namibia, Rwanda, Tanzania, Uganda,
  and Zambia. The Land Cover maps have been developed from LandSat Imagery (30m by
  30m) resolution using supervised classification. Image interpretation was done per
  scene. Images used for classification were selected based on seasonality, dry season
  images preferred. Land Cover maps are developed for two epochs: 2010 and 2000. For
  each year flexibility in image selection is allowed from previous and next year
  in each epoch. An epoch for 1990 is available in some of the project countries such
  as Malawi and Rwanda. Classification scheme used is based on Intergovernmental Panel
  on Climate Change (IPCC) 6 land over categories for Scheme I: Forestland, Grassland,
  Wetland, Cropland, Settlement and Other land. Classification Scheme II is informed
  by country specific interest, definitions, descriptions, mapping goals and policy
  statements and documents with guidance from IPCC Good Practice guidelines. Scheme
  II is such that it meets the country specific mapping standards and can be rolled
  back to the IPCC categories. Final map is taken through a 3pixel by 3pixel filter
  to eliminate salt and pepper effect and remove isolated pixels. Contact the Regional
  Centre for Mapping of Resources for Development at rcmrd@rcmrd.org for more information
  on GHG Land Cover Maps for Eastern and Southern Africa. [Source: This metadata record
  was automatically extracted from the GeoNode portal rcmrd]'
details: Users are advised to read and understand the metadata before access and use
  of the resources.
exposure:
- asset_type: null
  category: agriculture
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
- asset_type: null
  category: natural_environment
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
hazard: null
license: CC-BY-4.0
lineage:
  description: 'This land cover products were generated from LandSat thematic mapper
    (LandSat 5) data using supervised classification method. It involves the generation
    of training areas and then use maximum likelihood classification method to develop
    the land cover products. Other post classification procedures such as filtering,
    pixel/cell editing, density slicing etc. are used to refined the classification
    to generate final products. Accuracy assessment is conducted using actual field
    data and point interpretation from LandSat imagery which are randomly generated.
    The two most commonly used indices for assessing the map accuracy were the Overall
    accuracy and the KAPPA coefficient. The accuracy assessment results obtained for
    Rwanda 2010 Scheme I were: Overall Accuracy = 81.30%, Kappa Coefficient = 0.7407.'
  sources:
  - id: source_1
    license: null
    name: Patrick Kabatha
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://geoportal.rcmrd.org/catalogue/#/dataset/58
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Patrick Kabatha
  url: https://geoportal.rcmrd.org
purpose: Support ESA Country teams in developing and implementing land cover mapping
  efforts for Agriculture, Forestry and Land Use (AFOLU) sector in the development
  of Green House Gas (GHG) Inventory that meet IPCC specifications.
referenced_by: []
resources:
- access_url: https://geoportal.rcmrd.org/datasets/geonode:Rwanda_Landcover_2010_Scheme_I
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:4326
  description: 'Rwanda Land Cover 2010 Scheme I (OGC WMS: geonode Service)'
  download_url: https://geoportal.rcmrd.org/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:Rwanda_Landcover_2010_Scheme_I&format=image%2Fpng
  format: null
  id: resource_0
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: geonode Service'
- access_url: https://geoportal.rcmrd.org/datasets/geonode:Rwanda_Landcover_2010_Scheme_I
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wcs
  coordinate_system: EPSG:4326
  description: 'Rwanda Land Cover 2010 Scheme I (OGC WCS: geonode Service)'
  download_url: https://geoportal.rcmrd.org/geoserver/ows?service=WCS&version=2.0.1&request=DescribeCoverage&CoverageId=geonode__Rwanda_Landcover_2010_Scheme_I
  format: null
  id: resource_1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WCS: geonode Service'
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-rwa_rcmrd_landcover2010schemei
spatial:
  bbox:
  - 28.846756065804954
  - -2.893722314486977
  - 30.911365364631454
  - -1.021849585840687
  centroid: null
  countries:
  - RWA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: 2015
  duration: null
  end: null
  start: null
temporal_resolution: null
title: Rwanda Land Cover 2010 Scheme I
version: null
vulnerability: null
---
