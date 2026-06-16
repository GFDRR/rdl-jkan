---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldPop Research Group
    url: https://data.humdata.org/dataset/gridded-disaggregated-population-estimates-for-kenya-version-2-0
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: GRID3 project
    url: https://data.humdata.org/dataset/gridded-disaggregated-population-estimates-for-kenya-version-2-0
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/gridded-disaggregated-population-estimates-for-kenya-version-2-0
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/gridded-disaggregated-population-estimates-for-kenya-version-2-0
dataset_id: rdls_exp-ken_worldpop_griddeddisaggregatedpopul
description: 'These data were produced by the WorldPop Research Group at the University
  of Southampton. This work was part of the GRID3 project with funding from the United
  Nations Children''s Fund ( UNICEF ) - Population Modelling for use in Routine Health
  Planning and Monitoring project (contract no. 43335861). Projects partners included
  the Kenya Unicef Regional and Country Offices, WorldPop research group at the University
  of Southampton and the Center for International Earth Science Information Network
  in the Columbia Climate School at Columbia University. Assane Gadiaga (WorldPop)
  led the input processing and the modelling work following the Random Forest (RF)-based
  dasymetric mapping approach developed by Stevens et al. (2015). Thomas Abbott supported
  the covariates processing work. In-country engagements were done by David Kyalo,
  Olena Borkovska ( GRID3 , Maria Muniz (Unicef). Using the 2009 and 2019 census data
  from the Kenya''s National Bureau of Statistics (KNBS), the US Census Bureau released
  the census-based total population projections, population by age and gender and
  digital sub-counties boundaries. Duygu Cihan helped in the preparation of these
  input population data. Attila N Lazar, Edith Darin and Heather Chamberlain advised
  on the modelling procedure. The work was overseen by Attila N Lazar and Andy J Tatem.
  Recommended citations Gadiaga A. N., Abbott T. J., Chamberlain H., Lazar A. N.,
  Darin E., Tatem A. J. 2023. Census disaggregated gridded population estimates for
  Kenya (2022), version 2.0. University of Southampton. doi:10.5258/SOTON/WP00762
  License These data may be distributed using a Creative Commons Attribution 4.0 International
  (CC BY 4.0) License, specified in legal code. Contact release[at]worldpop.org for
  more information . The authors followed rigorous procedures designed to ensure that
  the used data, the applied method and thus the results are appropriate and of reasonable
  quality. If users encounter apparent errors or misstatements, they should contact
  WorldPop at release[at]worldpop.org. WorldPop , University of Southampton, and their
  sponsors offer these data on a ''where is, as is'' basis; do not offer an express
  or implied warranty of any kind; do not guarantee the quality, applicability, accuracy,
  reliability or completeness of any data provided; and shall not be liable for incidental,
  consequential, or special damages arising out of the use of any data that they offer..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/gridded-disaggregated-population-estimates-for-kenya-version-2-0]'
details: null
exposure:
- asset_type:
    description: Gridded disaggregated population estimates for Kenya at high spatial
      resolution, including age and gender disaggregation
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
hazard: null
license: CC-BY-4.0
lineage:
  description: Gridded population estimates were produced by WorldPop Research Group
    using census data and spatial disaggregation modelling techniques as part of the
    GRID3 project funded by UNICEF. The dataset includes total population counts and
    age-gender disaggregated estimates at high spatial resolution across Kenya for
    use in health planning and disaster risk assessment.
  sources:
  - id: source_1
    license: null
    name: WorldPop Research Group
    risk_data_type:
    - exposure
    type: model
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: GRID3 project
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/gridded-disaggregated-population-estimates-for-kenya-version-2-0
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Census
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This README file provides information about the data included in the
    data release, how it was produced, source data that were used, and known assumptions
    and limitations of the results.
  download_url: https://wopr.worldpop.org/download/546
  format: null
  id: resource_3d3e7279
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: KEN_population_v2_0_README.pdf
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This geotiff raster, at a spatial resolution of 3 arc-seconds (approximately
    100m at the equator), contains estimates of the total population size per grid
    cell across Kenya. NA values represent areas that were mapped as unsettled based
    on gridded building patterns derived from building footprints (Dooley and Tatem,
    2020). These data are stored as floating-point numbers rather than integers to
    avoid rounding errors in aggregated population totals for larger areas.
  download_url: https://wopr.worldpop.org/download/549
  format: null
  id: resource_7d02a7a8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: KEN_population_v2_0_gridded.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This zip file contains 40 GeoTIFF rasters representing estimated population
    counts for specific age and gender groups within grid cells of approximately 100m.
    We provide 36 rasters for the commonly reported age-gender groupings of sequential
    age classes for males and females separately. These are labelled with either an
    'm' (male) or an 'f' (female) followed by the number of the first year of the
    age class represented by the data. 'f0' and 'm0' are population counts of under
    1-year olds for females and males, respectively. 'f1' and 'm1' are population
    counts of 1 to 4 year olds for females and males, respectively. Over 4 years old,
    the age groups are in five-year bins labelled with a '5', '10', etc. Eighty year
    olds and over are represented in the groups 'f80' and 'm80'. We provide four additional
    rasters that represent demographic groups often targeted by programmes and interventions.
    These are 'under1' (all females and males under the age of 1), 'under5' (all females
    and males under the age of 5), 'under15' (all females and males under the age
    of 15) and 'f1549' (all females between the ages of 15 and 49, inclusive). These
    data were produced post-hoc by multiplying the total population counts provided
    in the KEN_population_v2_0_gridded.tif raster and age and gender proportions derived
    the US Census bureau age-gender projections for each sub-county. While this data
    represents population counts, values contain decimals, i.e. fractions of people.
    This is because both the input population data and age-gender proportions contain
    decimals. For this reason, it is advised to aggregate the rasters at a coarser
    scale. For example, if four grid cells next to each other have values of 0.25
    this indicates that there is 1 person of that age group somewhere in those four
    grid cells.
  download_url: https://wopr.worldpop.org/download/548
  format: null
  id: resource_6b55dabd
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: KEN_population_ v2_0_agegender.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This geotiff raster contains the rasterised administrative units used
    to perform the population disaggregation, with a spatial resolution of approximately
    100m grid cell (0.0008333 decimal degrees). The pixel values are IDs referring
    to the administrative boundary polygons (sub-counties) that match the corresponding
    units in the input population data.
  download_url: https://wopr.worldpop.org/download/547
  format: null
  id: resource_599c1689
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: KEN_population_ v2_0_mastergrid.tif
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-ken_worldpop_griddeddisaggregatedpopul
spatial:
  bbox: null
  centroid: null
  countries:
  - KEN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Gridded disaggregated population estimates for Kenya , version 2.0
version: null
vulnerability: null
---
