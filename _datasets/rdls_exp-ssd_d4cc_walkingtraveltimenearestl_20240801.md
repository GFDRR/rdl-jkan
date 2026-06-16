---
attributions:
- entity:
    affiliation: null
    email: null
    name: Child Poverty and Access to Services (CPAS) software
    url: https://data.humdata.org/dataset/south-sudan-walking-travel-time-to-nearest-level-iv-health-centre
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Data for Children Collaborative
  url: https://data.humdata.org/dataset/south-sudan-walking-travel-time-to-nearest-level-iv-health-centre
creator:
  affiliation: null
  email: null
  name: Data for Children Collaborative
  url: https://data.humdata.org/dataset/south-sudan-walking-travel-time-to-nearest-level-iv-health-centre
dataset_id: rdls_exp-ssd_d4cc_walkingtraveltimenearestl_20240801
description: 'A 100 m spatial resolution geotiff of walking travel time in seconds
  to nearest health facility in South Sudan. The data was generated using the Child
  Poverty and Access to Services (CPAS) software (10.5281/zenodo.4638563) and was
  created as part of the CPAS project within the Data for Children Collaborative.
  The travel time is calculated assuming walking speeds on all roads, tracks, paths
  and land cover types. A full description is available here a video description of
  the data is also available here Projection system is: GCS_WGS_1984 EPSG 4326 for
  all. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/south-sudan-walking-travel-time-to-nearest-level-iv-health-centre]'
details: "The United Nations Office for the Coordination of Humanitarian Affairs (OCHA)\
  \ Common Operational Datasets (COD) Administration Level 0 boundary polygons were\
  \ used in instances where geoBoundaries simplified polygons were not available.\
  \ Where countries were not included in the health facility data published by Maina\
  \ et al. (2019) we used data from the Global Health sites Mapping Project published\
  \ on Humanitarian Data Exchange (this included: Egypt, Libya, Tunisia, Algeria,\
  \ Morocco). For each country we removed health sites that were unlikely to offer\
  \ child focused services and vaccinations. Facilities that were removed included:\
  \ pharmacy, dentist, veterinary, caf\u221A\xA9/pharmacy, social facility. The accuracy\
  \ of the road data sets has not been validated, [Maina et al. (2019)](https://www.nature.com/articles/s41597-019-0142-2)"
exposure:
- asset_type:
    description: Walking travel time in seconds to nearest Level IV health facility
      across South Sudan at 100m resolution
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_1
  metrics:
  - dimension: disruption
    id: metric_1
    measurement:
      quantity_kind: length
      unit: null
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Walking travel time to health facilities was calculated using the CPAS
    software implementing a least cost path method. A friction/cost allocation surface
    was created representing travel effort across different land cover and road types,
    then used to compute minimum walking time in seconds to the nearest Level IV health
    centre for each 100m pixel across South Sudan.
  sources:
  - id: source_1
    license: null
    name: Child Poverty and Access to Services (CPAS) software
    risk_data_type:
    - exposure
    type: model
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/south-sudan-walking-travel-time-to-nearest-level-iv-health-centre
  rel: source
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://www.nature.com/articles/s41597-022-01274-w
- author_names: null
  date_published: null
  doi: null
  id: reference_2
  name: Methodology documentation
  url: https://zenodo.org/records/4638563#.YOycpRNKg6g
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This file is a zip archive containing travel time map in Geotiff format
    and a thumbnail image in PNG format.
  download_url: https://s3.eidf.ac.uk/eidf158-walkingtraveltimemaps/service_area_South%20Sudan_walking.tif
  format: null
  id: resource_d9ae81a1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: service-area-south-sudan-walking.tif
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-ssd_d4cc_walkingtraveltimenearestl_20240801
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
  start: '2024-08-01'
temporal_resolution: null
title: South Sudan Walking Travel Time to nearest Level IV health centre
version: null
vulnerability: null
---
