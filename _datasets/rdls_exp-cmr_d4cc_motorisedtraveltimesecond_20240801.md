---
attributions:
- entity:
    affiliation: null
    email: null
    name: Child Poverty and Access to Services (CPAS) software
    url: https://data.humdata.org/dataset/cameroon-motorised-travel-time-in-seconds-to-nearest-health-centre
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Data for Children Collaborative
  url: https://data.humdata.org/dataset/cameroon-motorised-travel-time-in-seconds-to-nearest-health-centre
creator:
  affiliation: null
  email: null
  name: Data for Children Collaborative
  url: https://data.humdata.org/dataset/cameroon-motorised-travel-time-in-seconds-to-nearest-health-centre
dataset_id: rdls_exp-cmr_d4cc_motorisedtraveltimesecond_20240801
description: 'A 100 m spatial resolution geotiff of motorised travel time in seconds
  to nearest health facility in Cameroon. The data was generated using the Child Poverty
  and Access to Services (CPAS) software (10.5281/zenodo.4638563) and was created
  as part of the CPAS project within the Data for Children Collaborative. The travel
  time is calculated assuming driving speeds of local public transport options on
  all-weather roads/asphalt roads and walking speeds on all other roads, tracks, paths
  and land cover types. A full description is available here a video description of
  the data is also available here Projection system is: GCS_WGS_1984 EPSG 4326 for
  all. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/cameroon-motorised-travel-time-in-seconds-to-nearest-health-centre]'
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
    description: Health facility accessibility measured by motorised travel time to
      nearest health centre
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
  description: Travel time surface generated using the CPAS least cost path method,
    which combines a friction surface representing motorised transport speeds on all-weather
    roads and walking speeds on other terrain types, applied to Cameroon at 100 m
    spatial resolution to quantify accessibility to health facilities.
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
- href: https://data.humdata.org/dataset/cameroon-motorised-travel-time-in-seconds-to-nearest-health-centre
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
  download_url: https://s3.eidf.ac.uk/eidf158-motorised-travel-time-maps/service_area_Cameroon_motorised.tif
  format: null
  id: resource_291f65ca
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: service-area-cameroon-motorised.tif
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-cmr_d4cc_motorisedtraveltimesecond_20240801
spatial:
  bbox: null
  centroid: null
  countries:
  - CMR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-08-01'
temporal_resolution: null
title: Cameroon Motorised Travel Time (in seconds) to nearest health centre
version: null
vulnerability: null
---
